from rest_framework import serializers
from .models import Interview



class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ['id', 'title', 'description', 'questions', 'date_interviewed']