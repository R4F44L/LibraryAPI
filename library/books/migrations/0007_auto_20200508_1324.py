# Generated by Django 3.0.6 on 2020-05-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20200508_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
