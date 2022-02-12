from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'name': 'VK'})

def WebDev(request):
    return render(request,'WebDev.html')

def CyberSec(request):
    return render(request,'CyberSec.html')

def CompArch(request):
    return render(request,'CompArch.html')

def DataAnalyst(request):
    return render(request,'DataAnalyst.html')

def CPP(request):
    return render(request,'CPP.html')

def ML(request):
    return render(request,'ML.html')