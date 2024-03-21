from . models import Task
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class Addtask(forms.ModelForm):
    class Meta():
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class EditTask(forms.ModelForm):
    class Meta():
        model = Task
        fields = ['title', 'description', 'due_date', 'completed', 'priority']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class Updatetask(forms.ModelForm):
    
    class Meta():
        model = Task
        fields = ['completed']

class RegisterUser(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
       