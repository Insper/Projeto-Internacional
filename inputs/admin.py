from django.contrib import admin
from .models import Candidate, Course, CourseDate, Timetable
from import_export import resources,fields
from import_export.admin import ExportActionMixin
from import_export.admin import ImportExportModelAdmin
import csv
from django.http import HttpResponse


admin.site.register(Candidate)
admin.site.register(Course)
admin.site.register(CourseDate)
# admin.site.register(Timetable)

class ExportCsvMixin:
    
    def export_as_csv(self, request, queryset):
    # Get database information
        qs = Timetable.objects.prefetch_related(
            'courses'
        )

        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export_file.csv"'

        writer = csv.writer(response)
        writer.writerow(['candidate','priority','courses'])

        for rule in qs:
            writer.writerow([rule.candidate.name, rule.priority,', '.join(c.name for c in rule.courses.all())])

        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("candidate", "priority", "get_courses")
    fields = ("candidate", "priority", "courses")

    # list_filter = ("is_immortal", "category", "origin", IsVeryBenevolentFilter)
    actions = ["export_as_csv"]
