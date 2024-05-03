from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Message(models.Model) :
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.body[0:50]
