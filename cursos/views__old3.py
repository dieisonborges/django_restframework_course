from html5lib import serialize
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Evaluation
from .serializers import CourseSerializer, EvaluationSerializer

"""
API Versão 1
"""

class CoursesAPIView(generics.ListCreateAPIView):
    """
    API de Cursos - LC
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API de Cursos - RUD
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EvaluationsAPIView(generics.ListCreateAPIView):
    """
    API de Avaliação de Cursos - LC
    """
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_queryset(self):
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        return self.queryset.all()


class EvaluationAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API de Avaliação de Cursos - RUD
    """
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_object(self):
        if self.kwargs.get('course_pk'):
            return get_object_or_404(
                    self.get_queryset(), 
                    course_id=self.kwargs.get('course_pk'),
                    pk=self.kwargs.get('evaluation_pk')
                )
        return get_object_or_404(
                self.get_queryset(),
                pk=self.kwargs.get('evaluation_pk')
            )


"""
API Versão 2
"""

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        course = self.get_object()
        serializer = EvaluationSerializer(course.evaluation.all(), many=True)
        return Response(serializer.data)

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer