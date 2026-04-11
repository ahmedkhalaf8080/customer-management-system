from django.contrib import admin
from . models import *
# Register your models here.

@admin.register(Category)
class CatrgoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass
