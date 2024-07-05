from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import Addtask, RegisterUser, Updatetask, EditTask
from .models import Task
from tasks.form import PasswordResetForm, UsernameForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout


def home(request):
    '''This function is used to render the home page of the application'''
    if request.user.is_authenticated:
        return redirect('into')
    else:
      return render(request, 'tasks/home.html')


def addtask(request):
    '''This function is used to add a task to the database'''
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
    '''This function is used to render the tasks of the logged in user'''
    user = request.user.id
    task = Task.objects.filter(user = user).order_by('created_on')
    context = {
        'tasks': task,

    }

    return render(request, 'tasks/yourtasks.html', context)


@login_required
def edit_task(request, id):
    '''This function is used to edit a task in the database'''
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
    '''This function is used to update a task in the database'''
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
    '''This function is used to render the details of a task'''
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
    '''This function is used to render the dashboard of the application'''
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
    '''This function is used to delete a task from the database'''
    task = Task.objects.get(id=id)
    task.delete()
    messages.success(request, 'Task deleted successfully')
    return redirect('yourtasks')

@login_required
def user_profile(request):
    '''This function is used to render the profile of the logged in user'''
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
    '''This function is used to register a new user'''
    if request.user.is_authenticated:
       logout(request)
       return redirect('register')
    register_form = RegisterUser()
    context = {
        'register': register_form
    }

    if request.method == 'POST':
        form = RegisterUser(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully')
            return redirect('account_login')
        else:
            messages.error(request, 'User not registered')
    else:
        form = RegisterUser()
    return render(request, 'tasks/register_users.html', context)


def custom_404(request, exception):
    '''This function is used to render the 404 page'''
    return render(request, 'tasks/404.html', status=404)

def redirect_account_signup(request):
    '''This function is used to redirect the user to the registration page'''
    return redirect('register')


def check_user(request):
    '''This function is used to check if a user exists in the database to reset the password'''
    username_form = UsernameForm()
    if request.method == 'POST':
        username_form = UsernameForm(request.POST)
        input_username = request.POST.get('username')
        username = User.objects.filter(username = input_username)
        if username.exists():
            messages.success(request, 'Username exists')
            username = request.POST.get('username')
            return redirect('password_reset1')
        else:
            messages.error(request, 'Username does not exist')
            username_form = UsernameForm()
            return render(request, 'password_reset.html', {'username_form': username_form, 'username': input_username})
    return render(request, 'password_reset.html', {'username_form': username_form})


def password_reset(request):
    '''This function is used to reset the password of a user'''
    password_form = PasswordResetForm()
    if request.method == 'POST':
        password_form = PasswordResetForm(request.POST)
        if password_form.is_valid():
            password = request.POST.get('password1')
            confirm_password = request.POST.get('password2')
            try:
               user = User.objects.get(username=request.POST.get('username'))
            except User.DoesNotExist:
                messages.error(request, 'User does not exist')
                return redirect('check_user')
            if password == confirm_password:
                user.password = make_password(password)
                user.save()
                messages.success(request, 'Password reset successfully')
                return redirect('account_login')
            else:
                messages.error(request, 'Passwords do not match')
                context = {
                    'password_form': password_form,
                    'username': request.POST.get('username')
                }
                return render(request, 'password_reset1.html', context)
        else:
            messages.error(request, 'Passwords do not match')
            password_form = PasswordResetForm()
            context = {
                'password_form': password_form,
                'username': request.POST.get('username')
            }
            return render(request, 'password_reset1.html', context)
    return render(request, 'password_reset1.html', {'password_form': password_form})