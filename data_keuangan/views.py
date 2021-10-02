from django.shortcuts import render, redirect
from .forms import UangForm
from .models import Uang

# Create your views here.
def keuangan_list(request):
	context = {
		'daftar_keuangan': Uang.objects.all()
	}
	return render(request, "data_keuangan/keuangan_list.html", context)

def keuangan_form(request, id=0):
	if request.method == "POST":
		if id == 0:
			form = UangForm(request.POST)
		else:
			ung = Uang.objects.get(pk=id)
			form = UangForm(request.POST, instance=ung)
		form.save()
		return redirect('/data_keuangan/list')

	else:
		if id == 0:
			form = UangForm()
		else:
			ung = Uang.objects.get(pk=id)
			form = UangForm(instance=ung)
		return render(request, "data_keuangan/keuangan_form.html", {'form': form})

def keuangan_delete(request, id):
	ung = Uang.objects.get(pk=id)
	ung.delete()
	return redirect('/data_keuangan/list')