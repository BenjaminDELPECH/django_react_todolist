from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import TodoList, Todo
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


name_unique_validator = UniqueTogetherValidator(
    queryset=TodoList.objects.all(),
    fields=['name', 'user'],

)


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'
        validators = [name_unique_validator]
