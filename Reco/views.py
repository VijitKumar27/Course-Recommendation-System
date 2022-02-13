from django.shortcuts import render
import pandas as pd
import numpy  as np

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

def questions12(request):
    return render(request,'questions12.html',{'name': 'vijitviku'})

def levels(request):
    ans1=int(request.POST['q1'])
    ans2=int(request.POST['q2'])
    ans3=int(request.POST['q3'])
    ans4=int(request.POST['q4'])
    ans5=int(request.POST['q5'])
    ans6=int(request.POST['q6'])
    ans7=int(request.POST['q7'])
    ans8=int(request.POST['q8'])
    ans9=int(request.POST['q9'])
    ans10=int(request.POST['q10'])
    res=ans1+ans2+ans3+ans4+ans5+ans6+ans7+ans8+ans9+ans10
    
    if(res>=140):
        df = pd.read_csv('static/clean_dataset.csv')
        webdev_df = df.query("subject=='Web Development'").sort_values('engagement',ascending=False)
        webdev_l1_df = webdev_df.query("level=='Beginner Level'").sort_values('engagement',ascending=False)
        course_name=webdev_l1_df.iloc[0]
        course_link=webdev_l1_df.iloc[0].url
        return render(request,'l3.html',{'name': 'vijitviku', 'course_name':course_name,'course_link':course_link})

    elif((res<140) and (res>=50)):
        df = pd.read_csv('static/clean_dataset.csv')
        webdev_df = df.query("subject=='Web Development'").sort_values('engagement',ascending=False)
        webdev_l1_df = webdev_df.query("level=='Beginner Level'").sort_values('engagement',ascending=False)
        course_name=webdev_l1_df.iloc[0]
        course_link=webdev_l1_df.iloc[0].url
        return render(request,'l2.html',{'name': 'vijitviku' , 'course_name':course_name,'course_link':course_link})

    else:
        df = pd.read_csv('static/clean_dataset.csv')
        webdev_df = df.query("subject=='Web Development'").sort_values('engagement',ascending=False)
        webdev_l1_df = webdev_df.query("level=='Beginner Level'").sort_values('engagement',ascending=False)
        course_name=webdev_l1_df.iloc[0]
        course_link=webdev_l1_df.iloc[0].url
        return render(request,'l1.html',{'name': 'vijitviku' , 'course_name':course_name,'course_link':course_link})

    
# def analysis_l1(request):
#      df = pd.read_csv('r','static/clean_dataset.csv')
#      webdev_df = df.query("subject=='Web Development'").sort_values('engagement',ascending=False)
#      webdev_l1_df = webdev_df.query("level=='Beginner Level'").sort_values('engagement',ascending=False)
#      course_name=webdev_l1_df.iloc[0]
#      course_link=webdev_l1_df.iloc[0].url
#      return render(request,'l1.html', {'course_name':course_name,'course_link':course_link})

     #webdev_l2_df = webdev_df.query("level=='Intermediate Level'").sort_values('engagement',ascending=False)
     #webdev_l3_df = webdev_df.query("level=='Expert Level'").sort_values('engagement',ascending=False)

     