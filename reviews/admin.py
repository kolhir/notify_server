from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html

from reviews.models import Review, ReviewProxy, Theme


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'ads_account', 'user_account', 'rating', 'theme_name')

    def theme_name(self, obj):
        return obj.theme.name

    theme_name.short_description = "Тема аккаунта"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(moderated=True)


@admin.register(ReviewProxy)
class ReviewProxyAdmin(admin.ModelAdmin):
    list_display = ('id', 'ads_account', 'user_account', 'rating', 'theme_name', 'review_actions')

    def theme_name(self, obj):
        return obj.theme.name

    theme_name.short_description = "Тема аккаунта"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(moderated=None)

    def review_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Одобрить</a>&nbsp;'
            '<a class="button" style="background-color: red;" href="{}">Отклонить</a>',
            reverse('admin:allow', args=[obj.pk]),
            reverse('admin:disallow', args=[obj.pk]))

    review_actions.short_description = 'Действия'
    review_actions.allow_tags = True

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<review_id>.+)/allow/$',
                self.admin_site.admin_view(self.allow),
                name='allow',
            ),
            url(
                r'^(?P<review_id>.+)/disallow/$',
                self.admin_site.admin_view(self.disallow),
                name='disallow',
            ),
        ]
        return custom_urls + urls

    def allow(self, request, review_id):
        review = Review.objects.get(id=review_id)
        review.moderated = True
        review.save()
        return HttpResponseRedirect('/admin/reviews/reviewproxy')

    def disallow(self, request, review_id):
        review = Review.objects.get(id=review_id)
        review.moderated = False
        review.save()
        return HttpResponseRedirect('/admin/reviews/reviewproxy')
