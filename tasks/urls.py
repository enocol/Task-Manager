from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('addtask/', views.addtask, name='addtask'),
    # path('yourtasks/', views.yourtasks, name='yourtasks'),
    # path('task/', views.yourtasks, name='task'),
    path('addtask/', views.addtask, name='addtask'),
    path('updatetask/<int:id>/', views.updatetask, name='updatetask'),
    path('taskdetails/<int:id>/', views.taskdetails, name='taskdetails'),
    path('taskdelete/<int:id>/', views.deletetask, name='deletetask'),
    path('completedtask/', views.completedtask, name='completedtask'),
    path('into/', views.into, name='into'),
    path('yourtasks/', views.YourTask.as_view(), name='yourtasks'),
]