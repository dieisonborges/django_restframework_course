import imp
from django.http import request
from html5lib import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from cursos.models import Evaluation

from .models import Course, Evaluation
from .serializers import CourseSerializer, EvaluationSerializer

class CourseAPIView(APIView):
    """
    API de Cursos
    """    
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class EvaluationAPIView(APIView):
    """
    API de Avaliação de Cursos
    """
    def get(self, request):
        evaluations = Evaluation.objects.all()
        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EvaluationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
