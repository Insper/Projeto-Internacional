from django.shortcuts import render, redirect
from .models import Candidate, Course, Timetable
import openpyxl
import os
from datetime import datetime


def check_same_values(list_values):
    for i in range(len(list_values)):
        for j in range(len(list_values)):
            if i != j and list_values[i] == list_values[j]:
                return True
    return False

def index(request): 
    if request.method == 'POST':
        name = request.POST.get('name')
        homeUniversity = request.POST.get('homeUniversity')
        courses1 = request.POST.getlist('courses1')        

        ects1 = request.POST.get('ECTS1')
        print("ESSE É O ECTS1: ", ects1)
        dataList1 = []
        for course1 in courses1: 
            print("Olha o nome do curso: ", course1)
            curso1_var = Course.objects.get(name=course1)
            datas1 = curso1_var.dates.all()
            dataListSameCourse1 = []
            for dataElement1 in datas1.iterator():
                elemento1 = dataElement1
                # print("Esse é o elemento:", elemento1)
                dataListSameCourse1.append(elemento1)
                # print("ESSE é o LIST DO DATA ELEMENT", dataListSameCourse1)
            
            dataList1.append(dataListSameCourse1)
        
        # print("LISTA DATA", dataList1)

        listaGeral1 = []
        for elemento1 in dataList1:
            for i in range(len(elemento1)):
                listaGeral1.append(elemento1[i])
        
        # print("LISTA GERAL: ", listaGeral1)

        Checando1 = check_same_values(listaGeral1)

        #------------------------------ opção 2 de curso------------------------------------

        courses2 = request.POST.getlist('courses2')       
        ects2 = request.POST.get('ECTS2')
        print("ESSE É O ECTS2: ", ects2) 

        dataList2 = []
        for course2 in courses2: 
            # print("Olha o nome do curso: ", course2)
            curso2_var = Course.objects.get(name=course2)
            datas2 = curso2_var.dates.all()
            dataListSameCourse2 = []
            for dataElement2 in datas2.iterator():
                elemento2 = dataElement2
                # print("Esse é o elemento:", elemento2)
                dataListSameCourse2.append(elemento2)
                # print("ESSE é o LIST DO DATA ELEMENT", dataListSameCourse2)
            
            dataList2.append(dataListSameCourse2)
        
        # print("LISTA DATA", dataList2)

        listaGeral2 = []
        for elemento2 in dataList2:
            for i in range(len(elemento2)):
                listaGeral2.append(elemento2[i])
        
        # print("LISTA GERAL: ", listaGeral2)

        Checando2 = check_same_values(listaGeral2)

        #---------------------------------------- opção 3 de curso----------------------------

        courses3 = request.POST.getlist('courses3')  
        ects3 = request.POST.get('ECTS3')
        print("ESSE É O ECTS3: ", ects3)      

        dataList3 = []
        for course3 in courses3: 
            # print("Olha o nome do curso: ", course3)
            curso3_var = Course.objects.get(name=course3)
            datas3 = curso3_var.dates.all()
            dataListSameCourse3 = []
            for dataElement3 in datas3.iterator():
                elemento3 = dataElement3
                # print("Esse é o elemento:", elemento3)
                dataListSameCourse3.append(elemento3)
                # print("ESSE é o LIST DO DATA ELEMENT", dataListSameCourse3)
            
            dataList3.append(dataListSameCourse3)
        
        print("LISTA DATA", dataList3)

        listaGeral3 = []
        for elemento3 in dataList3:
            for i in range(len(elemento3)):
                listaGeral3.append(elemento3[i])
        
        # print("LISTA GERAL: ", listaGeral3)

        Checando3 = check_same_values(listaGeral3)

        #--------------------------Conferindo os checks e postando tudo -----------------------

        if Checando1 or dataList1 == [] or int(ects1) < 18:
            return render(request, 'inputs/erro.html')
        elif Checando2 or dataList2 == [] or int(ects2) < 18:
            return render(request, 'inputs/erro.html')
        elif Checando3 or dataList3 == [] or int(ects3) < 18:
            return render(request, 'inputs/erro.html')
        else:
            #--------------- Postando a primeira opção --------------------------
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_date = now.strftime("%Y-%m-%d")
            date_time = current_date + " " + current_time

            candidate = Candidate(name = name, homeUniversity = homeUniversity, timestamp = date_time)
            candidate.save()

            candidato, criada1 = Candidate.objects.get_or_create(name=name, homeUniversity=homeUniversity)
            if criada1:
                candidato.save()
            # print("ESSE É O CANDIDATO!:", candidato)
            timetable1 = Timetable(priority= 1, candidate=candidato)
            timetable1.save()
            for course1 in courses1: 
                # print("Olha o nome do curso: ", course1)
                curso1 = Course.objects.get(name=course1)
                timetable1.courses.add(curso1)

            #----------------- Postando a segunda opção ----------------------------------

            # candidate2 = Candidate(name = name, homeUniversity = homeUniversity)
            # candidate2.save()
            candidato, criada2 = Candidate.objects.get_or_create(name=name, homeUniversity=homeUniversity)
            if criada2:
                candidato.save()
            # print("ESSE É O CANDIDATO!:", candidato)
            timetable2 = Timetable(priority= 2, candidate=candidato)
            timetable2.save()
            for course2 in courses2: 
                # print("Olha o nome do curso: ", course2)
                curso2 = Course.objects.get(name=course2)
                timetable2.courses.add(curso2)

            # ------------------------ Postando a terceira opção --------------------------------    
         
            candidato, criada3 = Candidate.objects.get_or_create(name=name, homeUniversity=homeUniversity)
            if criada3:
                candidato.save()
            print("ESSE É O CANDIDATO!:", candidato)
            timetable3 = Timetable(priority= 3, candidate=candidato)
            timetable3.save()
            for course3 in courses3: 
                # print("Olha o nome do curso: ", course3)
                curso3 = Course.objects.get(name=course3)
                timetable3.courses.add(curso3)
        
            return render(request, 'inputs/thanks.html')
    else:
        all_candidates = Candidate.objects.all()
        all_courses = Course.objects.all()
        available_courses = []
        for course in all_courses:
            if course.availability != "Unavailable":
                available_courses.append(course)

        # print("Esse é o AVAILABLE: ", available_courses)
        # print("Esse é o COURSES: ", all_courses)
        return render(request, 'inputs/index.html', {'candidates': all_candidates, 'courses': available_courses})


def telaVisualizacao(request):
    all_timetables = Timetable.objects.all()
    all_courses = Course.objects.all()
    available_courses = []
    for course in all_courses:
        if course.availability != "Unavailable":
            available_courses.append(course)
    # print(all_timetables)
    return render(request, 'inputs/timetables.html', {'timetables': all_timetables, 'courses': available_courses})
