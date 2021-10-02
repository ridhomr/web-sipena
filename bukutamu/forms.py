from django import forms
from django.forms import widgets
from .models import BukuTamu

class FormBukuTamu(forms.ModelForm):
    class Meta:
        model = BukuTamu
        fields = ('nama', 'alamat', 'email', 'instansi', 'keperluan', 'tanggal', 'telepon')
        labels = {
            'nama':'Nama Lengkap',
            'alamat':'Alamat',
            'email':'Email',
            'instansi':'Instansi',
            'keperluan':'Keperluan',
            'tanggal':'Tanggal',
            'telepon':'Telepon',
        }

        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'instansi': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'keperluan': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'tanggal': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'telepon': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
        }