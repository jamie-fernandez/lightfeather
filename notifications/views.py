from rest_framework import generics

from .models import Notification
from .serializers import NotificationSerializer


class ListNotification(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class DetailNotification(generics.RetrieveAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
