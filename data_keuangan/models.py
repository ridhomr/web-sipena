from django.db import models

# Create your models here.
class Keuangan(models.Model):
	nama_debit = models.CharField(max_length=50)

	def __str__(self):
		return self.nama_debit

class Uang(models.Model):
	nama = models.CharField(max_length=100)
	no_rekening = models.CharField(null=True, max_length=50)
	jumlah = models.CharField(null=True, max_length=200)
	keterangan = models.CharField(max_length=200)
	tanggal = models.DateField(null=True)
	debit = models.ForeignKey(Keuangan, on_delete=models.CASCADE)
