from django.db import models

# Create your models here.
class PointTypes(models.Model):
    name = models.CharField(verbose_name='Виды заведений', max_length=200, blank=False)

    class Meta:
        verbose_name = 'Вид заведения'
        verbose_name_plural = 'Виды заведений'

    def __str__(self):
        return self.name

class Point(models.Model):
    point_type = models.ForeignKey('PointTypes', on_delete=models.CASCADE, verbose_name='Тип заведения')
    short_name = models.CharField(verbose_name='Короткое название', max_length=200, blank=False)
    full_name = models.CharField(verbose_name='Полное название', max_length=200, blank=False)
    discription = models.TextField(verbose_name='Описание')
    slug = models.SlugField(blank=False)
    place_chords_x = models.FloatField(verbose_name='Кордината Х', blank=False)
    place_chords_y = models.FloatField(verbose_name='Кордината Y', blank=False)
    icon = models.ImageField(verbose_name='Фото', blank=False, null=True)

    class Meta:
        verbose_name = 'Заведение'
        verbose_name_plural = 'Заведения'

    def __str__(self):
        return self.short_name

class Room(models.Model):
    point = models.ForeignKey('Point', on_delete=models.CASCADE, verbose_name='Заведение')
    name = models.CharField(verbose_name='Название номера', max_length=200, blank=False)
    discription = models.TextField(verbose_name='Описание', blank=True)
    enable_count = models.PositiveIntegerField(verbose_name='Количество номеров', blank=False)
    guest_count = models.PositiveSmallIntegerField(verbose_name='Количество мест', blank=False)
    rooms_count = models.PositiveSmallIntegerField(verbose_name='Количество комнат', blank=False)
    bed_once_count = models.PositiveSmallIntegerField(verbose_name='Количество односпальных мест',)
    bed_two_count = models.PositiveSmallIntegerField(verbose_name='Количество двуспальных мест',)
    bed_sub_count = models.PositiveSmallIntegerField(verbose_name='Количество диванов',)
    is_wс = models.BooleanField(verbose_name='наличие туалета/ванной')
    is_balc = models.BooleanField(verbose_name='наличие балкона')
    is_tel = models.BooleanField(verbose_name='наличие телевизора')
    is_cond = models.BooleanField(verbose_name='наличие кондиционера')
    is_wifi = models.BooleanField(verbose_name='наличие вайфая')
    icon = models.ImageField(verbose_name='Фото', blank=False, null=True)

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'

    def __str__(self):
        return self.point.short_name + " - " + self.name



    
