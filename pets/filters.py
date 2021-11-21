import django_filters
from django_filters import DateFilter, DateTimeFilter

from .models import *


class OrderFilter(django_filters.FilterSet):
    start_date = DateTimeFilter(field_name="start_time", lookup_expr='gte')
    end_date = DateTimeFilter(field_name="start_time", lookup_expr='lte')

    class Meta:
        model = Event
        fields = '__all__'
        exclude = [id]
