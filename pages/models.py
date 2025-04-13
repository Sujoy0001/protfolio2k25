from django.db import models
from django.urls import reverse

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    institution = models.TextField(blank=True, null=True)
    degree = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, default="Location")
    contact_email = models.EmailField()
    experience_year = models.IntegerField(default=0, help_text="Years of experience in the field")
    
    
    # some extra details
    
    # my_email = models.EmailField()
    # my_phone = models.CharField(max_length=15)
    # my_location = models.CharField(max_length=100)
    # my_github = models.URLField()
    # my_linkedin = models.URLField()
    # my_twitter = models.URLField()

    def __str__(self):
        return self.name
      

class All_Skills(models.Model):
    skills_name = models.CharField(max_length=100)
    skills_img = models.ImageField(upload_to='skills_images/')
    proficiency = models.IntegerField(help_text="Proficiency level from 1 to 10")

    def __str__(self):
        return self.skills_name
    

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_type = models.CharField(max_length=20, choices=[('personal', 'Personal'), ('professional', 'Professional')])
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True, null=True , default='https://twitter.com/')
    preview_link = models.URLField(blank=True, null=True, default='https://twitter.com/')
    skills_used = models.ManyToManyField(All_Skills, blank=True)

    def __str__(self):
        return self.project_name
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})
    
    
class experience(models.Model):
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"


class extra_skills(models.Model):
    frist_skills = models.CharField(max_length=100)

    def __str__(self):
        return self.frist_skills
    
    
