from django.contrib import admin
from .models import Konser

@admin.register(Konser)
class KonserAdmin(admin.ModelAdmin):
    list_display = (
        'nama_konser',
        'artis',
        'lokasi',
        'tanggal',
        'harga_tiket',
        'tersedia'
    )

    list_filter = ('tersedia', 'lokasi')
    search_fields = ('nama_konser', 'artis')
    