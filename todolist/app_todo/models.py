from django.db import models
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True , max_length=200)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateField(blank=True , null=True)
    attachment = models.FileField(upload_to='attachments/' , blank=True , null=True)
    
    def __str__(self):
        return self.title