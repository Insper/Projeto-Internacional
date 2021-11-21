from django.shortcuts import render, redirect
from .models import Candidate, Course, Timetable
import openpyxl
import os

def index(request): 
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        homeUniversity = request.POST.get('homeUniversity')
        print(homeUniversity)
        candidate = Candidate(name = name, homeUniversity = homeUniversity)
        candidate.save()

        courses = request.POST.getlist('courses1')        

        candidato, criada = Candidate.objects.get_or_create(name=name, homeUniversity=homeUniversity)
        if criada:
            candidato.save()
        print("ESSE É O CANDIDATO!:", candidato)

        timetable = Timetable(priority= 1, candidate=candidato)
        timetable.save()

        data = 0
        for course in courses: 
            print("Olha o nome do curso: ", course)
            curso1 = Course.objects.get(name=course)
            timetable.courses.add(curso1)


        #------------------------------ opção 2 de curso------------------------------------

        courses = request.POST.getlist('courses2')        

        candidato, criada = Candidate.objects.get_or_create(name=name, homeUniversity=homeUniversity)
        if criada:
            candidato.save()
        print("ESSE É O CANDIDATO!:", candidato)

        timetable = Timetable(priority= 2, candidate=candidato)
        timetable.save()

        for course in courses: 
            print("Olha o nome do curso: ", course)
            curso2 = Course.objects.get(name=course)
            print(curso2)
            timetable.courses.add(curso2)

        #---------------------------------------- opção 3 de curso----------------------------

        courses = request.POST.getlist('courses3')        

        candidato, criada = Candidate.objects.get_or_create(name=name, homeUniversity=homeUniversity)
        if criada:
            candidato.save()
        print("ESSE É O CANDIDATO!:", candidato)

        timetable = Timetable(priority= 3, candidate=candidato)
        timetable.save()

        for course in courses: 
            print("Olha o nome do curso: ", course)
            curso3 = Course.objects.get(name=course)
            print(curso3)
            timetable.courses.add(curso3)        
        
        
        return redirect('index')
    else:
        all_candidates = Candidate.objects.all()
        all_courses = Course.objects.all()
        return render(request, 'inputs/index.html', {'candidates': all_candidates, 'courses': all_courses})