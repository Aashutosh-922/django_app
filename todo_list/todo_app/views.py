from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import TodoItem
from .serializers import TodoItemSerializer
from .models import Tag
from .serializers import TagSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace', 'create']


