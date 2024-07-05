from . models import Task
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError





class Addtask(forms.ModelForm):
    '''Form to create a task in the database'''
    class Meta():
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class EditTask(forms.ModelForm):
    '''Form to edit a task in the database'''
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    due_date = forms.DateTimeField()
    completed = forms.BooleanField(required=False, label='Mark as completed')
    class Meta():
        model = Task
        fields = ['title', 'description', 'due_date', 'completed', 'priority']
     

class Updatetask(forms.ModelForm):
    '''Form to update the completed field in the task table in the database'''
    completed = forms.BooleanField(required=False, label='Mark as completed')
    
    class Meta():
        model = Task
        fields = ['completed']



class RegisterUser(UserCreationForm):
    '''Custom Form to register a new user'''
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password',  help_text=(
            'Password must be at least 8 characters long.<br>'
            'Password must have letters and numbers.<br>'
            'Password cannot be all letters.<br>'
            'Password cannot be all numbers.'
        ), min_length=8)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password', help_text='Enter the same password as before, for verification', min_length=8)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    
   
       

class UsernameForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')

    class Meta:
        model = User
        fields = ['username']


class PasswordResetForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password1 = forms.CharField(widget=forms.PasswordInput, label='New Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    class Meta:
       model = User
       fields = ['username','password1', 'password2']