from .models import Task
from django.shortcuts import redirect, render
from django.contrib import messages
from .form import Addtask

# Create your views here.

def home(request):
    return render(request, 'tasks/home.html')


def addtask(request):
    form = Addtask()
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = Addtask(data=request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task added successfully')
            return redirect('yourtasks')
    else:
        form = Addtask()
    return render(request, 'tasks/addtask.html', context)


def yourtasks(request):
    task = Task.objects.all()
    context = {
        'tasks': task
    }
    return render(request, 'tasks/yourtasks.html', context)


