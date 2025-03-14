from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vehiculos(models.Model): 
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.DateField(null = True)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    sold = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Car: {self.name} create by {self.user.username}"