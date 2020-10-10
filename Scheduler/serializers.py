from rest_framework import serializers
from .models import TodoList, User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

