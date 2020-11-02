from django.contrib import admin

# Register your models here.

from .models import Lecture,Book,Course

admin.site.register(Lecture)
admin.site.register(Book)
admin.site.register(Course)
