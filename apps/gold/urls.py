print ('URLS')
from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index, name= "index"),
    url(r'^farm$', views.farm, name= "farm"),
    url(r'^house$', views.house, name= "house"),
    url(r'^cave$', views.cave, name= "cave"),
    url(r'^casino$', views.casino, name= "casino"),
]
