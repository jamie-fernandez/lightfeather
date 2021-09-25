from rest_framework import generics

from .models import Notification
from .serializers import NotificationSerializer


class ListNotification(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class DetailNotification(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
