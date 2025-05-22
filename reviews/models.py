from django.db import models
from pages.models import Project

class Review(models.Model):
    client_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    testimonial = models.TextField()
    client_photo = models.ImageField(upload_to='client_photos/', blank=True, null=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.project.project_name if self.project else 'No Project'}"
