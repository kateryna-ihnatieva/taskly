from .serializers import TaskSerializer
from rest_framework import viewsets
from .models import Task
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["is_completed", "priority"]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "updated_at", "is_completed", "priority_order"]
