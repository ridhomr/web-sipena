from django.urls import path 
from . import views 

urlpatterns = [
	path('', views.feedback_form, name='tambah_feedback'),
	path('<int:id>/', views.feedback_form, name='ubah_feedback'),
	path('delete/<int:id>/', views.feedback_delete, name='hapus_feedback'),
	path('list/', views.feedback_list, name='tampil_feedback'),
]