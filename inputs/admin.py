from django.contrib import admin
from .models import Candidate, Subject, SubjectDate


admin.site.register(Candidate)
admin.site.register(Subject)
admin.site.register(SubjectDate)