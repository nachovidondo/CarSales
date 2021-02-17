from django.contrib import admin
from . models import Category,Importation,Car
# Register your models here.
admin.site.register(Category)
admin.site.register(Importation)
admin.site.register(Car)