from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Projects, FA
from .serializers import FASerializer, ProjectSerializer
# Here we will write views which return serialized data using Serializers. Moreover, Class views are used subclassing
# APIViews.


class ProjectsAPIview(APIView):
    def get(self,request):
        ps = ProjectSerializer(Projects.objects.all(), many=True)
        return Response(ps.data)

class FAAPIView(APIView):
    def get(self, requests):
        result = FASerializer(FA.objects.all(), many=True)
        return Response(result.data)


class ProjectsList(generics.RetrieveDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer