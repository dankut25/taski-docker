"""Backend serializers."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """TaskSerializer serializer."""

    class Meta:
        """Meta class of TaskSerializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
