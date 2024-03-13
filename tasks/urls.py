from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('addtask/', views.addtask, name='addtask'),
    path('yourtasks/', views.yourtasks, name='yourtasks'),
    path('task/', views.yourtasks, name='task'),
    path('addtask/', views.addtask, name='addtask'),
    path('updatetask/<int:id>/', views.updatetask, name='updatetask'),
    path('taskdetails/<int:id>/', views.taskdetails, name='taskdetails'),
]