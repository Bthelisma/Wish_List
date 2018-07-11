from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^main$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^dashboard$', views.dashboard),
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^wish_item/(?P<id>\d+)$', views.show),
    url(r'^wish_item/(?P<id>\d+)/delete$', views.delete),
    url(r'^wish_item/(?P<id>\d+)/remove$', views.remove),
    url(r'^wish_item/(?P<id>\d+)/add$', views.join),


]
