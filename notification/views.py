from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework

from notification.filters import EventDateFilter
from notification.models import Notification
from notification.serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.filter()
    permission_classes = [IsAuthenticated]
    search_fields = ['title']
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filter_class = EventDateFilter

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(owner=user)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
