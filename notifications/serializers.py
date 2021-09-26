from rest_framework import serializers
from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('first_name', 'last_name',
                  'phone_number', 'email', 'supervisor')
