from rest_framework import serializers
from django.db.models import Avg

from .models import Course, Evaluation


class EvaluationSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {
                'write_only': True
                }
        }
        model = Evaluation
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'score',
            'created_at',
            'active',
        )
    def validate_score(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError('A avaliação precisa ser um inteiro entre 1 e 5')

class CourseSerializer(serializers.ModelSerializer):
    # Primary Key Related Field
    evaluation = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    average_evaluation = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'created_at',
            'active',
            'evaluation',
            'average_evaluation'
        )

    def get_average_evaluation(self, obj):
        average = obj.evaluation.aggregate(Avg('score')).get('score__avg')

        if average is None:
            return 0
        return round(average * 2) / 2