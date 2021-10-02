from django import forms 
from .models import Feedback

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ('nama', 'masukkan', 'saran')
		labels = {
			'nama':'nama lengkap',
			'masukkan':'masukkan anda',
			'saran':'saran anda',
		}