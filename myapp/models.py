from email.policy import default
from tkinter import CASCADE
from django.db import models

# Create your models here.


class Blog(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=1000000)
    upvote=models.IntegerField(default=0)
    downvote=models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE)
    content=models.CharField(max_length=10000)

    def __str__(self):
        return self.content
