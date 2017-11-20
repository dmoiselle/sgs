from django.contrib import admin

from .models import Shipment
from .models import Upload

class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['vessel', 'ata_eta_mom', 'ocean_del_terms', 'bl_teu', 'bl_feu', 'cf_agent', 'bl_number', 'qty_disch_loaded', 'commodity', 'pack', 'recipient_country', 'project_type', 'sgs_amount']

class UploadAdmin(admin.ModelAdmin):
    list_display = ['dateOfUpload', 'uploadedFile']

admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(Upload, UploadAdmin)
