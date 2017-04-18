from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect 
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, comment, User
from django.utils import timezone
from polls.urls import url
from .forms import commentForm, UserForm, SignupForm

a = ""

#class IndexView(generic.ListView):
#    template_name = 'polls/index1.html'
#    context_object_name = 'latest_question_list'
#    print(context_object_name)
#    def get_queryset(self):
#    	"""Return the last five published questions (not including those set to be published in the future)."""
#    	return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

def indexview(request, user_email):
	global a
	print(user_email)
	latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list, 'user_email' : user_email}
	print(context['user_email'])
	if(a == user_email):
		return render(request, 'polls/index1.html', context)
	else:
		raise Http404("Question Does Not Exist")
		
	
def detailview(request, user_email, pk):
	question_id = pk
	print(user_email, question_id)
	try:
		question = Question.objects.get(pk = question_id)
		context = {'question': question, 'user_email': user_email}
	except	Question.DoesNotExist:
		raise Http404("Question Does Not Exist")
	return render(request, 'polls/detail.html', context)

#class DetailView(generic.DetailView):
#    model = Question
#    template_name = 'polls/detail.html'
#    def get_queryset(self):
#        """
#        Excludes any questions that aren't published yet.
#        """
#        return Question.objects.filter(pub_date__lte=timezone.now())
    



class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def resultview(request, user_email, pk):
	print(user_email, question_id)
	try:
		question = Question.objects.get(pk = question_id)
		context = {'question': question, 'user_email': user_email}
	except	Question.DoesNotExist:
		raise Http404("Question Does Not Exist")
	return render(request, 'polls/results.html', context)



def vote(request, user_email, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
            'user_email': user_email,
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        context = {'question': question, 'user_email': user_email}
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'polls/results.html', context)
    print("********************************************************************************\n")
    
		
def add_comment(request, user_email, question_id):
    form = commentForm(request.POST or None)
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    template = "polls/data.html"
    question = get_object_or_404(Question, pk=question_id)
    print (request.POST, question_id)
    context = {"form" : form, "question_id" : question_id, 'user_email': user_email, 'latest_question_list': latest_question_list}
    if form.is_valid():
    	comment_text = form.cleaned_data["comment"]
    	time = timezone.now()
    	print(comment_text, time)
    	print("*****" + user_email)
    	c = question.comment_set.create(comment_text = comment_text, comment_date = time, comment_user = user_email)
    	return HttpResponseRedirect(reverse('polls:detail', args=(user_email, question_id)))
    return render(request, template, context)

def login(request):
	form = UserForm(request.POST or None)
	template = "polls/index.html"
	context = {"form" : form}
	global a
	print(request.POST)
	if form.is_valid():
		useremail_text = form.cleaned_data["Useremail"]
		password_text = form.cleaned_data["Password"]
		print(useremail_text, password_text)
		try:
			u = User.objects.get(user_email = useremail_text)
		except User.DoesNotExist:
			return render(request, 'polls/index.html', {
            	'error_message': "Email is wrong",
            	"form": form,
        	})
				
		print(u.user_password)
		
		if(password_text != u.user_password):
			return render(request, 'polls/index.html', {
            'error_message': "Email or password is wrong",
            "form": form,
        })
		else:
			a = useremail_text
			print(a)
			return HttpResponseRedirect("/polls/"+useremail_text)
	return render(request, template, context)
    
def signup(request):
	form = SignupForm(request.POST or None)
	template = "polls/signup.html"
	context = {"form" : form}
	print(request.POST)
	if form.is_valid():
		username_text = form.cleaned_data["Name"]
		useremail_text = form.cleaned_data["Email"]
		userpassword_text1 = form.cleaned_data["Password"]
		userpassword_text2 = form.cleaned_data["Password_Reenter"]
		usermobile_text = form.cleaned_data["Mobile_no"]
		if(userpassword_text1 == userpassword_text2):
			print(username_text, userpassword_text1, useremail_text, usermobile_text)
			u = User(user_name = username_text, user_email = useremail_text, user_password = userpassword_text1, user_mobile = usermobile_text)
			u.save()
			return HttpResponse("Sucessfully Registered\n<a href = '/polls'>Click Here For LOGIN</a>")
		else:
			return render(request, 'polls/signup.html', {
            'error_message': "Password doesn't match",
            "form": form,
        })
	return render(request, template, context)
	
def reg(request):
	context = {}
	return render(request, 'polls/reg.html', context)
    
    
    
    	    
