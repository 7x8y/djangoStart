from django.db import models

class CompanyManager(models.Manager):
    pass

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(("it", "it"), ("nonIt", "nonIt"), ("it2", "it2")))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    # Define a default manager for the Company model
    objects = CompanyManager()
