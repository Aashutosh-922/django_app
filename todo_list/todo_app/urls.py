from django.urls import path, include
from rest_framework import routers
from todo_app.views import TodoItemViewSet
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'todoitems', TodoItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include(router.urls)),
    path('api/', include('todo_app.urls')),
]
