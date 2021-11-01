from django.db import models
from .myFields import DayOfTheWeekField

class SubjectDate(models.Model):
    dayOfTheWeek = DayOfTheWeekField()
    hour = models.TimeField()

    def __str__(self):
        return  str(self.dayOfTheWeek)+" - "+str(self.hour)
class Subject(models.Model):
    name = models.CharField(max_length=200)
    professor = models.CharField(max_length=200)
    ect = models.IntegerField()
    duration = models.TimeField()
    dates = models.ManyToManyField(SubjectDate)

    def __str__(self):
        return  str(self.id)+". "+str(self.name)+" - "+str(self.professor)

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    homeUniversity = models.CharField(max_length=200)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return  str(self.id)+". "+str(self.name)
