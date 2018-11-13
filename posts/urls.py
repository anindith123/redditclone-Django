from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = "posts"

urlpatterns = [
    url(r'create/', views.create, name = "create"),
    url(r'(?P<pk>[0-9]+)/upvote',views.upvote, name = "upvote"),
    url(r'(?P<pk>[0-9]+)/downvote',views.downvote, name = "downvote"),
    url(r'posts/userview', views.userview, name = "userview")

    ]
    