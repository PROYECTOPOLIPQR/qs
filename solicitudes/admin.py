from django.contrib import admin
from solicitudes.models import Solicitud

admin.site.site_header = 'Administracion PQR'

class AdminSolicitud(admin.ModelAdmin):
	list_display = ["name"]
	search_fields = ["name"]
	class Meta:
		model = Solicitud

admin.site.register(Solicitud, AdminSolicitud)
