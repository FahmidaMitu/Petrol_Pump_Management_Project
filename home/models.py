from django.db import models

# Create your models here.


class Emenities(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Gas(models.Model):
    pump_name = models.CharField(max_length=100)
    pump_image = models.CharField(max_length=500)
    pump_address = models.TextField()
    available_amount = models.IntegerField()
    emenities = models.ManyToManyField(Emenities)

    def __str__(self):
        return self.pump_name
