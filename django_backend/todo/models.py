from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class TrackedModel(models.Model):
    last_updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class TodoList(TrackedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=255)


class Todo(TrackedModel):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    name = models.TextField(max_length=255)
