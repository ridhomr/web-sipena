from django.db import models
from django.db.models.enums import Choices

class Kuesioner(models.Model):
    Choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    Pilihan1 = models.CharField(choices=Choices, max_length=5)
    Pilihan2 = models.CharField(choices=Choices, max_length=5)
    Pilihan3 = models.CharField(choices=Choices, max_length=5)
    Pilihan4 = models.CharField(choices=Choices, max_length=5)
    Pilihan5 = models.CharField(choices=Choices, max_length=5)
    Pilihan6 = models.CharField(choices=Choices, max_length=5)
    Pilihan7 = models.CharField(choices=Choices, max_length=5)