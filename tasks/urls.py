from django.urls import path
from tasks import views



urlpatterns = [
    path('', views.home, name='home'),
    path('addtask/', views.addtask, name='addtask'),
    path('yourtasks/', views.yourtasks, name='yourtasks'),
    path('register/', views.register_user, name='register'),
    path('addtask/', views.addtask, name='addtask'),
    path('updatetask/<int:id>/', views.updatetask, name='updatetask'),
    path('taskdetails/<int:id>/', views.taskdetails, name='taskdetails'),
    path('taskdelete/<int:id>/', views.deletetask, name='deletetask'),
    path('into/', views.into, name='into'),
    path('task/edit/<int:id>', views.edit_task, name='edittask'),
    path('userprofile/', views.user_profile, name='userprofile'),
    path('accounts/checkuser/', views.check_user, name='check_user'),
    path('accounts/password_reset/', views.password_reset, name='password_reset1'),
]