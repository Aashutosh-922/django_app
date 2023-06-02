from django.urls import path, include
from rest_framework import routers
from todo_app.views import TodoItemViewSet

router = routers.DefaultRouter()
router.register(r'todoitems', TodoItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
