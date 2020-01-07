from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout)
]