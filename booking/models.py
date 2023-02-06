from django.db import models



# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=124)
    password = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20)
    fuel_amount = models.CharField(max_length=20)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.name
