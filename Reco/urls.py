from django.urls import path

from . import views

urlpatterns = {
    path('', views.index, name = "index"),
    path('WebDev', views.WebDev, name = "WebDev"),
    path('CyberSec', views.CyberSec, name = "CyberSec"),
    path('ML', views.ML, name = "ML"),
    path('CPP', views.CPP, name = "CPP"),
    path('DataAnalyst', views.DataAnalyst, name = "DataAnalyst"),
    path('CompArch', views.CompArch, name = "CompArch"),
    path('landing', views.landing, name = "landing"),
    path('questions', views.questions, name = "questions"),
    path('levels', views.levels, name = 'levels'),    
    path('l1', views.levels, name = 'l1'),
    path('l2', views.levels, name = 'l2'),
    path('l3', views.levels, name = 'l3')

}