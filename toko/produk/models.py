from django.db import models

class Konser(models.Model):
    nama_konser = models.CharField(max_length=100)
    artis = models.CharField(max_length=100)
    lokasi = models.CharField(max_length=100)
    tanggal = models.DateField()
    harga_tiket = models.IntegerField()
    tersedia = models.BooleanField(default=True)

    def __str__(self):
        return self.nama_konser