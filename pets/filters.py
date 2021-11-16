import django_filters
from .models import Event


class EventFilter(django_filters.FilterSet):
    title1 = django_filters.NumberFilter(field_name="title", lookup_expr='gte')
    title2 = django_filters.NumberFilter(field_name="title", lookup_expr='lte')

    class Meta:
        model = Event
        fields = '__all__'
