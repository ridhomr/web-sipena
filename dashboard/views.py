from django.shortcuts import render, redirect, HttpResponse
from kuesioner.models import Kuesioner
from bukutamu.models import BukuTamu
from bukutamu.forms import FormBukuTamu
from dashboard.resource import BukuTamuResource

# Create your views here.
def index(request):
    pilihan1_a = Kuesioner.objects.filter(Pilihan1=1).count
    pilihan1_b = Kuesioner.objects.filter(Pilihan1=2).count
    pilihan1_c = Kuesioner.objects.filter(Pilihan1=3).count
    pilihan1_d = Kuesioner.objects.filter(Pilihan1=4).count
    pilihan1_e = Kuesioner.objects.filter(Pilihan1=5).count

    pilihan2_a = Kuesioner.objects.filter(Pilihan2=1).count
    pilihan2_b = Kuesioner.objects.filter(Pilihan2=2).count
    pilihan2_c = Kuesioner.objects.filter(Pilihan2=3).count
    pilihan2_d = Kuesioner.objects.filter(Pilihan2=4).count
    pilihan2_e = Kuesioner.objects.filter(Pilihan2=5).count

    pilihan3_a = Kuesioner.objects.filter(Pilihan3=1).count
    pilihan3_b = Kuesioner.objects.filter(Pilihan3=2).count
    pilihan3_c = Kuesioner.objects.filter(Pilihan3=3).count
    pilihan3_d = Kuesioner.objects.filter(Pilihan3=4).count
    pilihan3_e = Kuesioner.objects.filter(Pilihan3=5).count

    pilihan4_a = Kuesioner.objects.filter(Pilihan4=1).count
    pilihan4_b = Kuesioner.objects.filter(Pilihan4=2).count
    pilihan4_c = Kuesioner.objects.filter(Pilihan4=3).count
    pilihan4_d = Kuesioner.objects.filter(Pilihan4=4).count
    pilihan4_e = Kuesioner.objects.filter(Pilihan4=5).count

    pilihan5_a = Kuesioner.objects.filter(Pilihan5=1).count
    pilihan5_b = Kuesioner.objects.filter(Pilihan5=2).count
    pilihan5_c = Kuesioner.objects.filter(Pilihan5=3).count
    pilihan5_d = Kuesioner.objects.filter(Pilihan5=4).count
    pilihan5_e = Kuesioner.objects.filter(Pilihan5=5).count

    pilihan6_a = Kuesioner.objects.filter(Pilihan6=1).count
    pilihan6_b = Kuesioner.objects.filter(Pilihan6=2).count
    pilihan6_c = Kuesioner.objects.filter(Pilihan6=3).count
    pilihan6_d = Kuesioner.objects.filter(Pilihan6=4).count
    pilihan6_e = Kuesioner.objects.filter(Pilihan6=5).count

    pilihan7_a = Kuesioner.objects.filter(Pilihan7=1).count
    pilihan7_b = Kuesioner.objects.filter(Pilihan7=2).count
    pilihan7_c = Kuesioner.objects.filter(Pilihan7=3).count
    pilihan7_d = Kuesioner.objects.filter(Pilihan7=4).count
    pilihan7_e = Kuesioner.objects.filter(Pilihan7=5).count

    context = {
        'pilihan1_a': pilihan1_a,
        'pilihan1_b': pilihan1_b,
        'pilihan1_c': pilihan1_c,
        'pilihan1_d': pilihan1_d,
        'pilihan1_e': pilihan1_e,

        'pilihan2_a': pilihan2_a,
        'pilihan2_b': pilihan2_b,
        'pilihan2_c': pilihan2_c,
        'pilihan2_d': pilihan2_d,
        'pilihan2_e': pilihan2_e,

        'pilihan3_a': pilihan3_a,
        'pilihan3_b': pilihan3_b,
        'pilihan3_c': pilihan3_c,
        'pilihan3_d': pilihan3_d,
        'pilihan3_e': pilihan3_e,

        'pilihan4_a': pilihan4_a,
        'pilihan4_b': pilihan4_b,
        'pilihan4_c': pilihan4_c,
        'pilihan4_d': pilihan4_d,
        'pilihan4_e': pilihan4_e,

        'pilihan5_a': pilihan5_a,
        'pilihan5_b': pilihan5_b,
        'pilihan5_c': pilihan5_c,
        'pilihan5_d': pilihan5_d,
        'pilihan5_e': pilihan5_e,

        'pilihan6_a': pilihan6_a,
        'pilihan6_b': pilihan6_b,
        'pilihan6_c': pilihan6_c,
        'pilihan6_d': pilihan6_d,
        'pilihan6_e': pilihan6_e,

        'pilihan7_a': pilihan7_a,
        'pilihan7_b': pilihan7_b,
        'pilihan7_c': pilihan7_c,
        'pilihan7_d': pilihan7_d,
        'pilihan7_e': pilihan7_e,
    }
    return render(request, 'dashboard/index.html', context)

def tabel_list(request):
    context = {
        'daftar_tabel': BukuTamu.objects.all()
    }
    return render(request, "dashboard/tabel.html", context)

def tabel_form(request, id=0):
    if request.method == "POST":
        if id == 0:
            form = FormBukuTamu(request.POST)
        else:
            buku = BukuTamu.objects.get(pk=id)
            form = FormBukuTamu(request.POST, instance=buku)
        form.save()
        return redirect('/dashboard/list')

    else:
        if id == 0:
            form = FormBukuTamu()
        else:
            buku = BukuTamu.objects.get(pk=id)
            form = FormBukuTamu(instance=buku)
        return render(request, "dashboard/tabel_form.html", {'form': form})
        
def tabel_delete(request, id):
    buku = BukuTamu.objects.get(pk=id)
    buku.delete()
    return redirect('/dashboard/list')

def export_xls_bukutamu(request):
    bukutamu = BukuTamuResource()
    dataset = bukutamu.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="laporan bukutamu.xls"'
    return response