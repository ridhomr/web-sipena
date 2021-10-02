from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="tambah"),
    path('', views.tabel_form, name="tambah_tabel"),
    path('<int:id>/', views.tabel_form, name="ubah_tabel"),
    path('delete/<int:id>/', views.tabel_delete, name="hapus_tabel"),
    path('list/', views.tabel_list, name="tampil_tabel"),
    path('bukutamu/export/xls', views.export_xls_bukutamu, name="export_xls_bukutamu"),
]
