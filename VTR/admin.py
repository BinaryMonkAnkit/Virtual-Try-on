# from django.contrib import admin
# from .models import Student
# # Register your models here.

# admin.site.register(Student)

# myapp/admin.py
from django.contrib import admin
from .models import Garment

@admin.register(Garment)
class GarmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'image','description','created_at')  # Columns to display in the admin list view
