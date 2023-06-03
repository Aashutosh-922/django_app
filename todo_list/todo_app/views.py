from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import TodoItem
from .serializers import TodoItemSerializer
from .models import Tag
from .serializers import TagSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from todo_app.models import TodoItem

def home(request):
    todos = TodoItem.objects.all()
    return render(request, 'home.htm', {'todos': todos})


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace', 'create']


class TodoItemListView(APIView):
    def get(self, request):
        todo_items = TodoItem.objects.all()
        serializer = TodoItemSerializer(todo_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoItemDetailView(APIView):
    def get(self, request, pk):
        todo_item = get_object_or_404(TodoItem, pk=pk)
        serializer = TodoItemSerializer(todo_item)
        return Response(serializer.data)

    def put(self, request, pk):
        todo_item = get_object_or_404(TodoItem, pk=pk)
        serializer = TodoItemSerializer(todo_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        todo_item = get_object_or_404(TodoItem, pk=pk)
        serializer = TodoItemSerializer(todo_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo_item = get_object_or_404(TodoItem, pk=pk)
        todo_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
