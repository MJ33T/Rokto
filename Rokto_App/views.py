from django.shortcuts import render
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'Rokto_App/index.html')


def find_donar(request):
    return render(request, 'Rokto_App/find_donar.html')


def new_donar(request):
    return render(request, 'Rokto_App/new_donar.html')
