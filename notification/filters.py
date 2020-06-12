from django_filters import DateRangeFilter, DateFilter, rest_framework

from notification.models import Notification


class EventDateFilter(rest_framework.FilterSet):
    date_range = DateRangeFilter(field_name='date', label="Period")

    class Meta:
        model = Notification
        fields = ['date', ]
