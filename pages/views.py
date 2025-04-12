from django.shortcuts import render
from .models import AboutMe, Project, All_Skills, experience, extra_skills

# Create your views here.

def example(request):
    about_info = AboutMe.objects.all()
    return render(request, 'example.html', {'aboutinfo': about_info})

def about(request):
    return render(request, 'about.html')


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})

def skill_page(request):
    skills = All_Skills.objects.all()
    return render(request, 'skills.html', {'skills': skills})

def index(request):
    about_info2 = AboutMe.objects.first() 
    Projects = Project.objects.all()
    exprate = experience.objects.all()
    skills = extra_skills.objects.all()
    total_projects = Projects.count()
    total_experience = exprate.count()
    return render(request, 'home.html', { 'aboutinfo': about_info2, 'projects': Projects, 'exprate': exprate, 'skills': skills, 'total_projects': total_projects, 'total_experience': total_experience })