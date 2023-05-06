from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from apps.task2.api_endpoints.vacancy.VacancyList.filters import VacancyFilter
from apps.task2.api_endpoints.vacancy.VacancyList.serializers import \
    VacancySerializer
from apps.task2.models import Vacancy


class VacancyList(ListAPIView):
    queryset = Vacancy.objects.filter(is_active=True).order_by("-created_at")
    serializer_class = VacancySerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = VacancyFilter


__all__ = ["VacancyList"]
