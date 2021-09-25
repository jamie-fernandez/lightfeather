from django.urls import path
from .views import ListNotification, DetailNotification

urlpatterns = [
    path('<int:pk>/', DetailNotification.as_view()),
    path('', ListNotification.as_view())
]
