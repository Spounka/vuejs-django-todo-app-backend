from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer


# Create your views here.

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
