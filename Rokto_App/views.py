from django.shortcuts import render


def home(request):
    return render(request, 'Rokto_App/index.html')
