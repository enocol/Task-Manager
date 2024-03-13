from . models import Task
from django import forms



class Addtask(forms.ModelForm):
    class Meta():
        model = Task
        fields = ['title', 'description', 'due_date', 'completed']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class Updatetask(forms.ModelForm):
    
    class Meta():
        model = Task
        fields = ['completed']
       