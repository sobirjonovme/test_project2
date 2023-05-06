from rest_framework import serializers

from apps.task2.models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ("id", "title", "description", "salary", "salary_from", "salary_to", "is_active")
