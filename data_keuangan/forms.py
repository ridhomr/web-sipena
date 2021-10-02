from django.forms import ModelForm
from django import forms 
from .models import Uang 

class UangForm(forms.ModelForm):
	class Meta:
		model = Uang 
		fields = ('nama', 'no_rekening', 'jumlah', 'keterangan', 'tanggal', 'debit')
		labels = {
			'nama':'Nama Lengkap',
			'no_rekening':'No Rekening',
			'jumlah':'Jumlah Uang',
			'keterangan':'sertakan keterangan',
			'tanggal':'Tanggal Transfer',
			'debit':'Kartu Debit',
		}

		widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'no_rekening': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'jumlah': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'keterangan': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'tanggal': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            
        }
