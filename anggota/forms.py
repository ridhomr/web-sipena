from django.forms import ModelForm
from django import forms 
from .models import Anggota

class AnggotaForm(forms.ModelForm):
	class Meta:
		model = Anggota
		fields = ('nama', 'email', 'telpon', 'rt', 'rw', 'alamat', 'tanggal_lahir', 'status', 'jurusan')
		labels = {
			'nama':'Nama Lengkap',
			'email':'Email',
			'telpon':'No Telpon',
			'rt':'RT',
			'rw':'RW',
			'alamat':'Alamat Anda',
			'tanggal_lahir':'Tanggal Lahir',
			'status':'Status',
			'jurusan':'Jurusan',
		}

		widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'telepon': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'rt': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'rw': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'tanggal_lahir': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            
        }