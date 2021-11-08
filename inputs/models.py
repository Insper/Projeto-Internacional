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

    def __str__(self):
        return  str(self.id)+". "+str(self.name)

class Timetable(models.Model):
    courses = models.ManyToManyField(Course)
    priority = models.IntegerField()
    candidate = models.ForeignKey(Candidate, null=True, on_delete=models.SET_NULL, related_name="timetable")

    def __str__(self):
        return  str(self.id)+". "+str(self.candidate.name)+"-"+str(self.priority)



