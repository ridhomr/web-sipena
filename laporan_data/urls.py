from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', views.home, name='file'),
	path('list/', views.laporan_list, name='tampil_anggota'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)