from django.contrib import admin
from .models import PointTypes, Point, Room, News

# Register your models here.
admin.site.register(PointTypes)
admin.site.register(Point)
admin.site.register(Room)
admin.site.register(News)