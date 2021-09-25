from django.db import models


class Notification(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=320)
    supervisors = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
