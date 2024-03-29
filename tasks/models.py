from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
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
