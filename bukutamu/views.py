from django.shortcuts import render, redirect
from .forms import FormBukuTamu
from .models import BukuTamu

# Create your views here.
# def form(request, id=0):
#     form = FormBukuTamu()
#     if request.method == 'POST':
#         form = FormBukuTamu(request.POST)
#         if form.is_valid():
#             form.save()
#         if id == 0:
#             form = FormBukuTamu(request.POST)
#         else:
#             tamu = BukuTamu.objects.get(pk=id)
#             form = FormBukuTamu(request.POST, instance = tamu)
#         return redirect('/bukutamu/')
#     else:
#         if id == 0:
#             form = FormBukuTamu()
#         else:
#             tamu = BukuTamu.objects.get(pk=id)
#             form = FormBukuTamu(instance = tamu)
#         return render(request, 'bukutamu/index.html', {'form':form})

def form(request):
    form = FormBukuTamu()
    if request.method == 'POST':
        form = FormBukuTamu(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/bukutamu/')
    
    return render(request, 'bukutamu/index.html', {'form': form})