from rest_framework import serializers

from reviews.models import Review, Theme


class ThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = ("id", "name")


class CreateReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ("id", "ads_account", "user_account", "rating", "theme")

    def create(self, validated_data):
        request = self.context.get("request")
        return Review.objects.create(**validated_data, user=request.user, moderated=None)


class ReviewSerializer(serializers.ModelSerializer):
    theme = ThemeSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ("id", "ads_account", "user_account", "rating", "theme")







