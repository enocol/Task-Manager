from .models import Task
from django.shortcuts import redirect, render
from django.contrib import messages
from .form import Addtask, Updatetask
from django.views.decorators.cache import never_cache
from django.views import generic

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


# def yourtasks(request):
#     task = Task.objects.all().order_by('created_on')
#     context = {
#         'tasks': task,
#     }

#     return render(request, 'tasks/yourtasks.html', context)

class YourTask(generic.ListView):
    queryset = Task.objects.all().order_by('created_on')
    template_name = 'tasks/yourtasks.html'
   



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



def completedtask(request):
    completed= Task.objects.filter(completed=True)
    context = {
        'completed_tasks': completed
    }
    return render(request, 'tasks/completedtask.html', context)


def into(request):
    user = request.user
    usertasks = Task.objects.filter(user=user)
    completed = usertasks.filter(completed=True).count()
    pending = usertasks.filter(completed=False).count()
    context = {
        'completed': completed,
        'pending': pending,
    }


    return render(request, 'tasks/into.html', context)



def deletetask(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    messages.success(request, 'Task deleted successfully')
    return redirect('yourtasks')


