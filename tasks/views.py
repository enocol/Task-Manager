from datetime import datetime

from django.forms import ValidationError
from .models import Task
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate 
from .form import Addtask, RegisterUser, Updatetask, EditTask
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('into')
    else:
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
            form.save()
            messages.success(request, 'Task added successfully')
           
            return redirect('yourtasks')
    else:
        messages.error(request, '')
        form = Addtask()

    return render(request, 'tasks/addtask.html', {messages: messages, 'form': form})

@login_required
def yourtasks(request):
    user = request.user.id
    task = Task.objects.filter(user = user).order_by('created_on')
    context = {
        'tasks': task,

    }

    return render(request, 'tasks/yourtasks.html', context)
@login_required
def edit_task(request, id):
    task = Task.objects.get(id=id)
    edit_task = EditTask(instance=task)
    context = {
        'edittask': edit_task
    }

    if request.method == 'POST':
        form = EditTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully')
            return redirect('yourtasks')
    return render(request, 'tasks/edit_task.html', context)
   


@login_required
def updatetask(request, id):
    task = Task.objects.get(id=id)
    form = Addtask(instance=task)
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = Addtask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully')
            return redirect('yourtasks')
    return render(request, 'tasks/updatetask.html', context)

@login_required
def taskdetails(request, id):
    task = Task.objects.get(id=id)
    completed = Updatetask(instance=task)
    context = {
        'task': task,
        'completed': completed
    }

    if request.method == 'POST':
        completed = Updatetask(request.POST, instance=task)
        if completed.is_valid():
            completed.save()
            messages.success(request, 'Task updated successfully')
            return redirect('yourtasks')
    return render(request, 'tasks/taskdetails.html', context)


@login_required
def into(request):
    user = request.user.id
    usertasks = Task.objects.filter(user=user)
    completed = usertasks.filter(completed=True).count()
    pending = usertasks.filter(completed=False).count()
    messages.success(request, '')
    context = {
        'completed': completed,
        'pending': pending,
    }


    return render(request, 'tasks/into.html', context)


@login_required
def deletetask(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    messages.success(request, 'Task deleted successfully')
    return redirect('yourtasks')


def user_profile(request):
    user = request.user.id
    usertasks = Task.objects.filter(user=user)
    completed = usertasks.filter(completed=True).count()
    pending = usertasks.filter(completed=False).count()
    context = {
        'completed': completed,
        'pending': pending,
    }
    return render(request, 'tasks/user_profile.html', context)


def register_user(request):
    register_form = RegisterUser()
    context = {
        'register': register_form
    }

    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully')
            return redirect('account_login')
    else:
        form = RegisterUser()
    return render(request, 'tasks/register_users.html', context)


def custom_404(request, exception):
    return render(request, 'tasks/404.html', status=404)


