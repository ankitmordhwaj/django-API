from django.contrib import admin
from .models import Drink
from .models import Student

admin.site.register(Drink)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']