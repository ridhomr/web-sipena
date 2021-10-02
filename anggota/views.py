from django.shortcuts import render, redirect, HttpResponse
from .forms import AnggotaForm
from .models import Anggota
from anggota.resource import AnggotaResource


# Create your views here.
def anggota_list(request):
	context = {
		'daftar_anggota': Anggota.objects.all()
	}
	return render(request, "anggota/anggota_list.html", context)

def anggota_form(request, id=0):
	if request.method == "POST":
		if id == 0:
			form = AnggotaForm(request.POST)
		else:
			agt = Anggota.objects.get(pk=id)
			form = AnggotaForm(request.POST, instance=agt)
		form.save()
		return redirect('/anggota/list')

	else:
		if id == 0:
			form = AnggotaForm()
		else:
			agt = Anggota.objects.get(pk=id)
			form = AnggotaForm(instance=agt)
		return render(request, "anggota/anggota_form.html", {'form':form})

def anggota_delete(requet, id):
	agt = Anggota.objects.get(pk=id)
	agt.delete()
	return redirect('/anggota/list')

def export_xls(request):
	anggota = AnggotaResource()
	dataset = anggota.export()
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment; filename="laporan anggota.xls"'
	return response