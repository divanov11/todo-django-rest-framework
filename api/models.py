from django.db import models

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField(null=True, blank=True)
  completed = models.BooleanField(default=False, blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
      
  def __str__(self):
    return self.title