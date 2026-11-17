from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('links/', views.links, name='links'),
    path('feedback/', views.feedback, name='feedback'),
    path('registration/', views.registration, name='registration'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:parameter>/', views.blogpost, name='blogpost'),
    path('newpost/', views.newpost, name='newpost'),
    path('video/', views.videopost, name='videopost'),
]