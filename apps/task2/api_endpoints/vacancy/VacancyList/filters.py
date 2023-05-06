from django.db.models import Q
from django_filters import rest_framework as filters

from apps.task2.models import Vacancy


class VacancyFilter(filters.FilterSet):
    salary = filters.CharFilter(method="filter_by_salary")

    class Meta:
        model = Vacancy
        fields = ["salary"]

    def filter_by_salary(self, queryset, name, value):
        vacancies = queryset.filter(
            Q(salary__exact=value) |
            Q(
                Q(salary_from__lte=value) & Q(salary_to__gte=value)
            )
        )

        return vacancies
