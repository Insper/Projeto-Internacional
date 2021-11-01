from django.shortcuts import render, redirect
from .models import Candidate
import openpyxl
import os

def index(request): 
    if request.method == 'POST':
        name = request.POST.get('name')
        homeUniversity = request.POST.get('homeUniversity')
        input = Candidate(name = name, homeUniversity = homeUniversity)
        input.save()
        return redirect('index')
    else:
        all_inputs = Candidate.objects.all()
        return render(request, 'inputs/index.html', {'inputs': all_inputs})