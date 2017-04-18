import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)    
    


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text        

class comment(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	comment_text = models.CharField(max_length = 1000)
	comment_date = models.DateTimeField(auto_now_add = True, auto_now = False)
	comment_user = models.CharField(max_length = 200)
	
class User(models.Model):
	user_name = models.CharField(max_length=200)
	user_email = models.CharField(max_length=200)
	user_password = models.CharField(max_length=200)
	user_mobile = models.CharField(max_length = 10)

