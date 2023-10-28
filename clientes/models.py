from django.db import models

# Create your models here.
class Cliente(models.Model):
    name     = models.CharField(max_length=70)
    password = models.CharField(max_length=50)
    email    = models.CharField(max_length=80, default="example@.com")
    number   = models.CharField(max_length=20, default="55 55555-5555")
    

    def __str__(self) -> str:
        return self.name
