from os import name
from django.db import router
from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
        CoursesAPIView,
        CourseAPIView,
        EvaluationsAPIView,
        EvaluationAPIView,
        CourseViewSet,
        EvaluationViewSet
    )

router = SimpleRouter()
router.register('cursos', CourseViewSet)
router.register('avaliacoes', EvaluationViewSet)

urlpatterns = [
    path('cursos/', CoursesAPIView.as_view(), name='cursos'),
    path('curso/<int:pk>/', CourseAPIView.as_view(), name='curso'),
    path('curso/<int:course_pk>/avaliacoes/', EvaluationsAPIView.as_view(), name='curso_avaliacoes'),
    path('curso/<int:course_pk>/avaliacao/<int:evaluation_pk>/', EvaluationAPIView.as_view(), name='curso_avaliacao'),

    path('avaliacoes/', EvaluationsAPIView.as_view(), name='avaliacoes'),
    path('avaliacao/<int:evaluation_pk>/', EvaluationAPIView.as_view(), name='avaliacao'),
]
