from django.urls import path
from . import views 

urlpatterns = [
	path('', views.keuangan_form, name='tambah_keuangan'),
	path('<int:id>/', views.keuangan_form, name='ubah_keuangan'),
	path('delete/<int:id>/', views.keuangan_delete, name='hapus_keuangan'),
	path('list/', views.keuangan_list, name='tampil_keuangan'),
]