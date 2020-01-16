from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^details/(?P<nonprofit_id>\d+)$', views.details),
    url(r'^account$', views.account),
    url(r'^search$', views.search),
    url(r'^main$', views.main),
    url(r'^search_results$', views.search_results),
    url(r'^add/(?P<nonprofit_id>\d+)$', views.add_list),
    url(r'^remove/(?P<nonprofit_id>\d+)$', views.remove_list),
    url(r'^remove_details/(?P<nonprofit_id>\d+)$', views.remove_list_details),
]