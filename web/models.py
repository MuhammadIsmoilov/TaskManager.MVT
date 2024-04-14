from django.db import models

# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    father_name = models.CharField(max_length = 50)
    date_of_birth = models.DateField(auto_now=False)
    adress = models.CharField(max_length = 100)
    bio = models.TextField()
    is_married = models.BooleanField()

    def __str__(self):
        return self.first_name + " " + self.last_name

