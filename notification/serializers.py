
from rest_framework import serializers

from notification.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField(required=False, allow_null=True)
    date = serializers.DateTimeField()

    class Meta:
        model = Notification
        fields = ("id", "title", "date", "description")

    def create(self, validated_data):
        request = self.context.get("request")
        return Notification.objects.create(**validated_data, owner=request.user)




