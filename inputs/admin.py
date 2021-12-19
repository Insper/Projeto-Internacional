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
        writer.writerow(['candidate', 'timestamp', 'priority','courses', 'course- priority I', 'course- priority II', 'course- priority III'])

        course_priority1 = {}
        course_priority2 = {}
        course_priority3 = {}
        for rule in qs:
            for curso in rule.courses.all():
                # print("Esse é o courses.all ", (rule.courses.all()))
                print("Esse é o priority: ", rule.priority)
                if rule.priority == 1 and curso.name not in course_priority1:
                    print("entrei")
                    course_priority1[curso.name] = 1
                elif rule.priority == 1 and curso.name in course_priority1:
                    course_priority1[curso.name]+= 1
                elif rule.priority == 2 and curso.name not in course_priority2:
                    course_priority2[curso.name] = 1
                elif rule.priority == 2 and curso.name in course_priority2:
                    course_priority2[curso.name] += 1
                elif rule.priority == 3 and curso.name not in course_priority3:
                    course_priority3[curso.name] = 1
                elif rule.priority == 3 and curso.name in course_priority3:
                    course_priority3[curso.name] += 1
                
        print ("PRIORIDADE 1: ", course_priority1)
        print ("PRIORIDADE 2: ", course_priority2)
        print ("PRIORIDADE 3: ", course_priority3)


        for rule in qs:
            informacao = str(rule.candidate.timestamp)
            splitTimestamp = informacao.split(" ")
            splitDate = splitTimestamp[0].split("-")
            date = splitDate[2] + "/" + splitDate[1] + "/" + splitDate[0]

            splitTime1 = str(splitTimestamp[1]).split("+")
            splitTime2 = str(splitTime1[0]).split(":")
            time = splitTime2[0] + ":" + splitTime2[1] + ":" + splitTime2[2]
            dateTime = date + " " + time
            writer.writerow([rule.candidate.name, dateTime, rule.priority,', '.join(c.name for c in rule.courses.all()), ", ".join(key+":"+str(value) for key,value in course_priority1.items()), ", ".join(key2+":"+str(value2)  for key2,value2 in course_priority2.items()), ", ".join(key3+":"+str(value3)  for key3,value3 in course_priority3.items())])


        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("candidate", "priority", "get_courses")
    fields = ("candidate", "priority", "courses")

    # list_filter = ("is_immortal", "category", "origin", IsVeryBenevolentFilter)
    actions = ["export_as_csv"]
