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
    
    def export_as_csv_timetable(self, request, queryset):
    # Get database information
        qs = Timetable.objects.prefetch_related(
            'courses'
        )

        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export_file.csv"'

        writer_table1 = csv.writer(response)
        
        writer_table1.writerow(['candidate', 'timestamp', 'priority','courses'])


        for rule in qs:
            informacao = str(rule.candidate.timestamp)
            splitTimestamp = informacao.split(" ")
            splitDate = splitTimestamp[0].split("-")
            date = splitDate[2] + "/" + splitDate[1] + "/" + splitDate[0]

            splitTime1 = str(splitTimestamp[1]).split("+")
            splitTime2 = str(splitTime1[0]).split(":")
            time = splitTime2[0] + ":" + splitTime2[1] + ":" + splitTime2[2]
            dateTime = date + " " + time
            writer_table1.writerow([rule.candidate.name, dateTime, rule.priority,', '.join(c.name for c in rule.courses.all())])

        return response

    export_as_csv_timetable.short_description = "Export Timetable"

    def export_as_csv_coursesPorPriority(self, request, queryset):
    # Get database information
        qs = Timetable.objects.prefetch_related(
            'courses'
        )

        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export_file.csv"'

        fieldnames = ['course', 'priority I', 'priority II', 'priority III']

        writer_table2 = csv.writer(response)
        writer_table2.writerow(fieldnames)
        
        # writer_table2.writerow(['course- priority I', 'course- priority II', 'course- priority III'])

        course_priority1 = {}
        course_priority2 = {}
        course_priority3 = {}
        for rule in qs:
            for curso in rule.courses.all():
                # print("Esse é o courses.all ", (rule.courses.all()))
                # print("Esse é o priority: ", rule.priority)
                if rule.priority == 1 and curso.name not in course_priority1:
                    # print("entrei")
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
            
        listaCourses = []
        for curso1 in course_priority1:
            if curso1 not in listaCourses:
                listaCourses.append(curso1)
        for curso2 in course_priority2:
            if curso2 not in listaCourses:
                listaCourses.append(curso2)
        for curso3 in course_priority3:
            if curso3 not in listaCourses:
                listaCourses.append(curso3)

        print("ESSA É A LISTA: ", listaCourses)


        valuesCoursePriority1 = []
        valuesCoursePriority2 = []
        valuesCoursePriority3 = []

        for curso1 in listaCourses:
            if curso1 not in course_priority1 :
                    valuesCoursePriority1.append('0')
            for data1 in course_priority1:
                if data1 == curso1:
                    valuesCoursePriority1.append(str(course_priority1[data1]))

        for curso2 in listaCourses:
            if curso2 not in course_priority2 :
                    valuesCoursePriority2.append('0')
            for data2 in course_priority2:
                if data2 == curso2:
                    valuesCoursePriority2.append(str(course_priority2[data2]))      

        for curso3 in listaCourses:
            if curso3 not in course_priority3 :
                    valuesCoursePriority3.append('0')
            for data3 in course_priority3:
                if data3 == curso3:
                    valuesCoursePriority3.append(str(course_priority3[data3]))
 
                        
        print ("PRIORIDADE 1: ", course_priority1)
        print ("PRIORIDADE 2: ", course_priority2)
        print ("PRIORIDADE 3: ", course_priority3)

        print("VALORES: ", valuesCoursePriority1)
        print("VALORES: ", valuesCoursePriority2)
        print("VALORES: ", valuesCoursePriority3)

        for i in range(len(listaCourses)):
            writer_table2.writerow([listaCourses[i], valuesCoursePriority1[i], valuesCoursePriority2[i], valuesCoursePriority3[i]])

        return response

    export_as_csv_coursesPorPriority.short_description = "Export Courses por Priority"


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("candidate", "priority", "get_courses")
    fields = ("candidate", "priority", "courses")

    # list_filter = ("is_immortal", "category", "origin", IsVeryBenevolentFilter)
    actions = ["export_as_csv_timetable", "export_as_csv_coursesPorPriority"]
