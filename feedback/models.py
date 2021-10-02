from django.db import models

# Create your models here.
class Feedback(models.Model):
	nama = models.CharField(max_length=100)
	masukkan = models.CharField(max_length=200)
	saran = models.CharField(max_length=200)

	def __str__(self):
		return self.nama