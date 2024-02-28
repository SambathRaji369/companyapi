# company/models.py
from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=255, unique=True)
    email_id = models.EmailField(unique=True)
    company_code = models.CharField(max_length=5, blank=True, null=True, unique=True)
    strength = models.PositiveIntegerField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
