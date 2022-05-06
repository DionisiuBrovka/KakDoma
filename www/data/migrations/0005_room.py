# Generated by Django 4.0.3 on 2022-05-06 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_point_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название номера')),
                ('discription', models.TextField(verbose_name='Описание')),
                ('enable_count', models.PositiveIntegerField(verbose_name='Количество номеров')),
                ('guest_count', models.PositiveSmallIntegerField(verbose_name='Количество мест')),
                ('rooms_count', models.PositiveSmallIntegerField(verbose_name='Количество комнат')),
                ('bed_once_count', models.PositiveSmallIntegerField(verbose_name='Количество односпальных мест')),
                ('bed_two_count', models.PositiveSmallIntegerField(verbose_name='Количество двуспальных мест')),
                ('bed_sub_count', models.PositiveSmallIntegerField(verbose_name='Количество диванов')),
                ('is_wс', models.BooleanField(verbose_name='наличие туалета/ванной')),
                ('is_balc', models.BooleanField(verbose_name='наличие балкона')),
                ('is_tel', models.BooleanField(verbose_name='наличие телевизора')),
                ('is_cond', models.BooleanField(verbose_name='наличие кондиционера')),
                ('is_wifi', models.BooleanField(verbose_name='наличие вайфая')),
                ('point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.point', verbose_name='Заведение')),
            ],
            options={
                'verbose_name': 'Номер',
                'verbose_name_plural': 'Номера',
            },
        ),
    ]