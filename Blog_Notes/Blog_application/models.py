from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)


    class Meta:
        managed=True
        db_table='Notes'