from django.contrib import admin
from .models import Group, Lesson, Teacher, Timetable

admin.site.register(Group)
admin.site.register(Lesson)
admin.site.register(Teacher)
admin.site.register(Timetable)
