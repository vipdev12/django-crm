from django.contrib import admin

from .models import Flat, Category, Manager

# Register your models here.
admin.site.register(Flat)
admin.site.register(Category)
admin.site.register(Manager)