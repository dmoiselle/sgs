from django.db import models

class Shipment(models.Model):
    vessel = models.CharField(max_length=200)
    ata_eta_mom = models.DateField()
    ocean_del_terms = models.CharField(max_length=10)
    bl_teu = models.IntegerField()
    bl_feu = models.IntegerField()
    cf_agent = models.CharField(max_length=20)
    bl_number = models.CharField(max_length=50)
    qty_disch_loaded = models.DecimalField(max_digits=10, decimal_places=3)
    commodity = models.CharField(max_length=50)
    pack = models.CharField(max_length=10)
    recipient_country = models.CharField(max_length=20)
    project_type = models.CharField(max_length=20)
    sgs_amount = models.IntegerField()

class Upload(models.Model):
    dateOfUpload = models.DateField()
    uploadedFile = models.FileField()
