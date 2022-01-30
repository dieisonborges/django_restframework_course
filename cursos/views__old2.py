from html5lib import serialize
from rest_framework import generics

from .models import Course, Evaluation
from .serializers import CourseSerializer, EvaluationSerializer


class CourseAPIView(generics.ListCreateAPIView):
    """
    API de Cursos
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EvaluationAPIView(generics.ListCreateAPIView):
    """
    API de Avaliação de Cursos
    """
    queryset = Course.objects.all()
    serializer_class = EvaluationSerializer