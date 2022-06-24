from django.contrib import admin
from .models import FastFood,Chinese
# Register your models here.
class FastFoodAdmin(admin.ModelAdmin):
    list_display=('name','price')
admin.site.register(FastFood,FastFoodAdmin)
class ChineseAdmin(admin.ModelAdmin):
    list_display=('name','price')
admin.site.register(Chinese,ChineseAdmin)