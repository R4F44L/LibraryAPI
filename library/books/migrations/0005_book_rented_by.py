# Generated by Django 3.0.6 on 2020-05-08 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0004_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rented_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='rented_books', to=settings.AUTH_USER_MODEL),
        ),
    ]
