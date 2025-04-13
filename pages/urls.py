from django.urls import path
from django.http import HttpResponseNotFound
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('skills/', views.skills, name='skills_page'),
    path('example/', views.example, name='example'),
    path('contact/', views.contact, name='contact'),
    path('review/', views.review, name='review'),
    path('404-test/', lambda request: HttpResponseNotFound(render(request, 'example.html'))),
]