from django.db import models

# Create your models here.

class BukuTamu(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    telepon = models.CharField(null=True, max_length=100)
    email = models.EmailField(max_length=100)
    instansi = models.CharField(max_length=100)
    tanggal = models.DateField(null=True)
    keperluan = models.CharField(max_length=100)

    def __str__(self):
        return self.nama