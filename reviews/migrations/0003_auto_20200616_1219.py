# Generated by Django 3.0.7 on 2020-06-16 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_moderated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hiddenreview',
            old_name='hidden_ads_account',
            new_name='hidden_account',
        ),
        migrations.RemoveField(
            model_name='hiddenreview',
            name='hidden_user_account',
        ),
    ]
