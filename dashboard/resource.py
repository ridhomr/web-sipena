from import_export import resources 
from bukutamu.models import BukuTamu
from import_export.fields import Field 

class BukuTamuResource(resources.ModelResource):
	nama_id__nama = Field(attribute='id', column_name='id')

	class Meta:
		model = BukuTamu
		fields = ['nama', 'alamat', 'email', 'instansi', 'keperluan', 'tanggal', 'telepon']
		export_order =  ['nama', 'alamat', 'email', 'instansi', 'keperluan', 'tanggal', 'telepon']
