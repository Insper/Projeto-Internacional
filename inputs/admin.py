from django.contrib import admin
from .models import Candidate, Course, CourseDate, Timetable


admin.site.register(Candidate)
admin.site.register(Course)
admin.site.register(CourseDate)
admin.site.register(Timetable)