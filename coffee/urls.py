from django.urls import path
from . import views
from .views import handle_action

urlpatterns = [
    path('',views.home),
    path('coffee/', views.home2, name='home2'), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('message/', views.message, name='message'),
    path('logout/', views.logout, name='logout'),
     path('handle-action/', handle_action, name='handle_action'),

]