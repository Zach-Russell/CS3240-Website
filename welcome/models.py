from django.db import models

class Tutor(models.Model):
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name + " " + self.last_name
# Create your models here.
