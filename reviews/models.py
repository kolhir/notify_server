from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Тема аккаунта"
        verbose_name_plural = "Темы аккаунтов"


class Review(models.Model):
    ads_account = models.CharField(max_length=300, verbose_name="Брали рекламу у блогера")
    user_account = models.CharField(max_length=300, verbose_name="Мой аккаунт")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.FloatField(verbose_name="Оценка")
    theme = models.ForeignKey(Theme, null=True, on_delete=models.SET_NULL)
    moderated = models.BooleanField(null=True, default=None)

    class Meta:
        verbose_name = "Одобренный отзыв"
        verbose_name_plural = "Одобренные отзывы"


class HiddenReview(models.Model):
    hidden_account = ArrayField(models.CharField(max_length=300), default=list)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class ReviewProxy(Review):

    class Meta:
        proxy = True
        verbose_name = "Отзыв на модерации"
        verbose_name_plural = "Отзывы на модерации"
