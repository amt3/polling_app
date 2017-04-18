from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
	url(r'^$', views.login, name='index'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^reg/$', views.reg, name='reg'),
    url(r'^(?P<user_email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.com)/$', views.indexview, name='index'),
    url(r'^(?P<user_email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.com)/(?P<pk>[0-9]+)/$', views.detailview, name='detail'),
    url(r'^(?P<user_email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.com)/(?P<pk>[0-9]+)/results/$', views.resultview, name='results'),
    url(r'^(?P<user_email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.com)/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^(?P<user_email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.com)/(?P<question_id>[0-9]+)/add_comment/$', views.add_comment, name='add_comment'),
]
