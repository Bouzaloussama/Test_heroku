from django.conf.urls import url
from django.urls import path

#from . views import 
from . import views

app_name = 'ontologie'


urlpatterns = [
	url(r'^$', views.Ontologie, name='Ontologie'),
	#url(r'^All_class$', views.All_class, name='All_class'),
	#url(r'^(?P<id>\d+)$', views.Post, name='Post'),
]