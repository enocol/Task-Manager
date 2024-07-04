from django.contrib import admin
from django.urls import path, include
from tasks import views
from django.conf.urls import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('accounts/', include("allauth.urls")),
    
]

handler404 = 'tasks.views.custom_404'
