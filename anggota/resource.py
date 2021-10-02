from import_export import resources 
from anggota.models import Anggota
from import_export.fields import Field 

class AnggotaResource(resources.ModelResource):
	jurusan_id__nama = Field(attribute='jurusan_id', column_name='jurusan')

	class Meta:
		model = Anggota
		fields = ['nama', 'email', 'telpon', 'rt', 'rw', 'alamat', 'tanggal_lahir', 'status', 'jurusan']
		export_order = ['nama', 'email', 'telpon', 'rt', 'rw', 'alamat', 'tanggal_lahir', 'status', 'jurusan']