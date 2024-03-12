from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'tasks/home.html')


def addtask(request):
    return render(request, 'tasks/addtask.html')


def yourtasks(request):
    return render(request, 'tasks/yourtasks.html')
