import requests

from rest_framework.response import Response
from rest_framework import viewsets


class SupervisorListView(viewsets.ViewSet):
    def sort_supervisors(self, response):
        sorted_managers = []

        for manager in response:
            if manager["jurisdiction"].isnumeric():
                continue
            else:
                sorted_managers.append(
                    f'{manager["jurisdiction"]} - {manager["firstName"]}, {manager["lastName"]}')
        return sorted_managers

    def list(self, request):
        supervisorAPI = 'https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers'
        response = requests.get(supervisorAPI)

        sorted_response = self.sort_supervisors(response.json())

        return Response(data=sorted_response)
