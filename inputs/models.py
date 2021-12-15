from django.db import models
from .myFields import DayOfTheWeekField, Status

class CourseDate(models.Model):
    dayOfTheWeek = DayOfTheWeekField()
    hour = models.TimeField()

    def __str__(self):
        return  str(self.dayOfTheWeek)+" - "+str(self.hour)

class Course(models.Model):
    name = models.CharField(max_length=200)
    professor = models.CharField(max_length=200)
    ects = models.IntegerField()
    duration = models.TimeField()
    dates = models.ManyToManyField(CourseDate)
    availability = Status()

    def __str__(self):
        return  str(self.id)+". "+str(self.name)+" - "+str(self.professor)


class Candidate(models.Model):
    name = models.CharField(max_length=200)
    homeUniversity = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=False, editable=True)
    
    def __str__(self):
        splitTimestamp = str(self.timestamp).split(" ")
        splitDate = splitTimestamp[0].split("-")
        date = splitDate[2] + "/" + splitDate[1] + "/" + splitDate[0]

        splitTime1 = str(splitTimestamp[1]).split("+")
        splitTime2 = str(splitTime1[0]).split(":")
        time = splitTime2[0] + ":" + splitTime2[1] + ":" + splitTime2[2]
        dateTime = date + " " + time

        return dateTime + "| " +  str(self.name)
    

class Timetable(models.Model):
    courses = models.ManyToManyField(Course)
    priority = models.IntegerField()
    candidate = models.ForeignKey(Candidate, null=True, on_delete=models.SET_NULL, related_name="timetable")

    def get_courses(self):
        return ",".join([p.name for p in self.courses.all()])

    def __str__(self):
        return  str(self.id)+". "+str(self.candidate.name)+"-"+str(self.priority)



