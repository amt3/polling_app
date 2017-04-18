from django import forms 

class commentForm(forms.Form):
    comment = forms.CharField(required = True)
    
class UserForm(forms.Form):
	Useremail = forms.CharField(required = True)
	Password = forms.CharField(widget=forms.PasswordInput)
	
class SignupForm(forms.Form):
	Name = forms.CharField(required = True)
	Email = forms.CharField(required = True)
	Password = forms.CharField(widget=forms.PasswordInput)
	Password_Reenter = forms.CharField(widget=forms.PasswordInput) 
	Mobile_no = forms.CharField(required = True)
 
