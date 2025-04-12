from django.contrib import admin
from .models import AboutMe, Project, All_Skills, experience, extra_skills

admin.site.register(AboutMe)

admin.site.register(Project)

admin.site.register(All_Skills)

admin.site.register(experience)

admin.site.register(extra_skills)
