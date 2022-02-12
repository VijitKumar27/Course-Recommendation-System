from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'name': 'VK'})

def WebDev(request):
    return render(request,'WebDev.html',{'name': 'vijitviku'})

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

def landing(request):
    return render(request,'landing.html',{'name': 'vijitviku'})

def questions(request):
    return render(request,'questions.html',{'name': 'vijitviku'})

def levels(request):
    ans1=int(request.POST['num1'])
    

def l1(request):
    return render(request,'l1.html',{'name': 'vijitviku'})