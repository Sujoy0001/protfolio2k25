from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.project_list, name='projects_list'),
    path('skills/', views.skill_page, name='skills_page'),
    path('example/', views.example, name='example'),
]