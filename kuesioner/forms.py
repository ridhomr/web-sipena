from django.shortcuts import render
from bukutamu.views import form
from django import forms
from django.forms import widgets
from .models import Kuesioner

class FormKuesioner(forms.ModelForm):
    Choices = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    Pilihan1 = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)
    Pilihan2 = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)
    Pilihan3 = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)
    Pilihan4 = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)
    Pilihan5 = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)
    Pilihan6 = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)
    Pilihan7 = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)

    class Meta:
        model = Kuesioner
        fields = ('Pilihan1', 'Pilihan2', 'Pilihan3', 'Pilihan4', 'Pilihan5', 'Pilihan6', 'Pilihan7')