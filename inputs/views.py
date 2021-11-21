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
        some_var = request.POST.getlist('checks[]')
        print("SOME VAR", some_var)
        for c in courses:
            print(c.name)
            elemento = Course(name=c)
            elemento.save()
        
        #  for i in range(len(lista_de_tags)):
        #     elemento = Tag(tag=lista_de_tags[i])
        #     elemento.save()
        #     quote.tags.add(elemento)
            

        print("Esses são os cursos: ", courses)
        # print("ESSES SAO COURSES: ", courses)
        # priority = request.POST.get(1)
        # candidato, criado = Candidate.objects.get_or_create(name=name)
        
        candidato, criada = Candidate.objects.get_or_create(name=name, homeUniversity=homeUniversity)
        if criada:
            candidato.save()
        print("ESSE É O CANDIDATO!:", candidato)
        
        timetable = Timetable(courses= courses, priority= 1, candidate=candidato)
        timetable.save()
     

        return redirect('index')
    else:
        all_candidates = Candidate.objects.all()
        all_courses = Course.objects.all()
        return render(request, 'inputs/index.html', {'candidates': all_candidates, 'courses': all_courses})