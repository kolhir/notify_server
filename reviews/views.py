from django.db.models import Q
from django.http import JsonResponse
from rest_framework import viewsets, status, mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from reviews.models import Review, HiddenReview, Theme
from reviews.serializers import ReviewSerializer, CreateReviewSerializer, ThemeSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateReviewSerializer
        else:
            return ReviewSerializer

    def get_queryset(self):
        if self.request.auth:
            print(self.request.user)
            obj, created = HiddenReview.objects.get_or_create(user=self.request.user)
            return Review.objects.filter(moderated=True).exclude(Q(ads_account__in=obj.hidden_account) |
                                                   Q(user_account__in=obj.hidden_account))
        return Review.objects.filter(moderated=True)


class ThemeViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer


class HiddenReviewsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        account_name = request.data.get('account_name')
        if account_name:
            obj, created = HiddenReview.objects.get_or_create(user=request.user)
            if account_name not in obj.hidden_account:
                obj.hidden_account.append(account_name)
                obj.save()
        return JsonResponse({"data": "Successfully hidden"}, status=status.HTTP_200_OK)
