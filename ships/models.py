from django.db import models


class Ship(models.Model):
    model = models.CharField(max_length=30)
    make = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    banner = models.ImageField()

    def __str__(self):
        return self.model
