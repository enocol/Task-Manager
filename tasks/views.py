from .models import Task


from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'tasks/home.html')


def addtask(request):
    return render(request, 'tasks/addtask.html')


def yourtasks(request):
    task = Task.objects.all()
    context = {
        'tasks': task
    }
    return render(request, 'tasks/yourtasks.html', context)


