from django.shortcuts import render, HttpResponse, redirect
from .models import FilesUpload

def home(request):
	if request.method == "POST":
		file2 = request.FILES["file"]
		document = FilesUpload.objects.create(file=file2)
		document.save()
		return redirect("list/")
	return render(request, "laporan_data/laporan_form.html")


def laporan_list(request):
	context = {
		'daftar_laporan': FilesUpload.objects.all()
	}
	return render(request, "laporan_data/laporan_list.html", context)