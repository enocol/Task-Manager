from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class Task(models.Model):
    ''''This class is used to create a task model in the database'''
    OPTIONS = (
        ('Low', 'Low'),
        ('Normal', 'Normal'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=7, choices=OPTIONS, default='Normal')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} was created by: {self.user}"
    
    def clean(self):
        super().clean()
        due_date = self.due_date
        if due_date and timezone.is_naive(due_date):
            due_date = timezone.make_aware(due_date, timezone.get_current_timezone())
        
        if due_date <= timezone.now():
            raise ValidationError('Due date can not be a date that has already passed.')
    
   
