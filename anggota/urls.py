from django.urls import path
from . import views 
from django.conf.urls.static import static

urlpatterns = [
	path('', views.anggota_form, name='tambah_anggota'),
	path('<int:id>/', views.anggota_form, name='ubah_anggota'),
	path('delete/<int:id>/', views.anggota_delete, name="hapus_anggota"),
	path('list/', views.anggota_list, name='tampil_anggota'),
	path('anggota/export/xls/', views.export_xls, name='export_xls'),
]
