from rest_framework import viewsets

from api_information.models import Agent
from api_information.serializers import AgentSerializer


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
