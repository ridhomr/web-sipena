from django.shortcuts import render, redirect
from .forms import FormKuesioner
from .models import Kuesioner

# Create your views here.
# def form(request, id=0):
#     form = FormKuesioner()
#     if request.method == 'POST':
#         form = FormKuesioner(request.POST)
#         print(form.is_valid())
#         if form.is_valid():
#             form.save()
#         if id == 0:
#             form = FormKuesioner(request.POST)
#         else:
#             hasil = Kuesioner.objects.get(pk=id)
#             form = FormKuesioner(request.POST, instance = hasil)
#         return redirect('/kuesioner/')
#     else:
#         if id == 0:
#             form = FormKuesioner()
#         else:
#             hasil = Kuesioner.objects.get(pk=id)
#             form = FormKuesioner(instance = hasil)
#         return render(request, 'kuesioner/index.html', {'form':form})
#     return render(requst, 'kuisioner/index.html', {'form': form})
def form(request):
    form = FormKuesioner()
    if request.method == 'POST':
        form = FormKuesioner(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/')
    
    return render(request, 'kuesioner/index.html', {'form': form})