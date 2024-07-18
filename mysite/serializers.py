from rest_framework import serializers
from .models import TodoList, User

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']
