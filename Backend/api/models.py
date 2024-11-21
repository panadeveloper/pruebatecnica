from django.db import models
from django.contrib.postgres.fields import JSONField

class DatabaseConfig(models.Model):
    host = models.CharField(max_length=255)
    port = models.IntegerField()
    namedb = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    query = models.TextField()
    
    def __str__(self):
        return self.namedb
    
    class ExtractionLog(models.Model):
        extraction_date = models.DateTimeField(auto_now_add=True)
        success = models.BooleanField()
        details = models.TextField(blank=True, null=True)
        
        def __str__(self):
            return f"Extraction on {self.extraction_date} - success {self.success}"
        
    class Factura(models.Model):
        fecha = models.DateField()
        total = models.DecimalField(max_digits=10, decimal_places=2)
        cliente_id = models.IntegerField()
        descripcion = models.TextField(blank=True, null=True)
        
        def __str__(self):
            return f"Factura {self.id} - Monto {self.total}"
    
    

    

    
