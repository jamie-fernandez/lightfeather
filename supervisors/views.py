import requests

from rest_framework.response import Response
from rest_framework import viewsets


class SupervisorListView(viewsets.ModelViewSet):
    def list(self):
        supervisorAPI = 'https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers'
        response = requests.get(supervisorAPI)

        return Response(data=response.json())
