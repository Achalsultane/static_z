from django.db import models
from django.db import models
# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.fullname
    
from django.db import models

class CompanyLogo(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Logo {self.id}"