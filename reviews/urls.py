from django.urls import path
from rest_framework.routers import DefaultRouter

from reviews.views import ReviewViewSet, HiddenReviewsView, ThemeViewSet

app_name = "reviews"

urlpatterns = [
    path('hide_reviews/', HiddenReviewsView.as_view()),
    path('theme/', ThemeViewSet.as_view({'get': 'list'})),
    path('',  ReviewViewSet.as_view({'get': 'list', 'post': 'create'}))
]
