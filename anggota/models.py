from django.db import models

# Create your models here.
class Jurusan(models.Model):
	nama_jurusan = models.CharField(max_length=100)

	def __str__(self):
		return self.nama_jurusan

class Anggota(models.Model):
	nama = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	telpon = models.CharField(null=True, max_length=100)
	rt = models.CharField(max_length=100)
	rw = models.CharField(max_length=100)
	alamat = models.CharField(max_length=200)
	tanggal_lahir = models.DateField(null=True)
	status = models.CharField(max_length=50)
	jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE)

	def __str__(self):
		return self.nama