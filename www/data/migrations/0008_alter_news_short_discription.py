# Generated by Django 4.0.4 on 2022-05-07 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='short_discription',
            field=models.CharField(blank=True, max_length=200, verbose_name='Краткое описание'),
        ),
    ]
