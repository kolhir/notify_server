# Generated by Django 3.0.7 on 2020-06-16 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='moderated',
            field=models.BooleanField(default=False),
        ),
    ]