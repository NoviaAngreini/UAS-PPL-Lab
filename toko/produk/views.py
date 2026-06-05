from django.shortcuts import render, redirect, get_object_or_404
from .models import Konser


# Home
def home(request):
    semua_konser = Konser.objects.all()

    return render(request, 'home.html', {
        'konser_list': semua_konser
    })


# Daftar konser
def daftar_konser(request):
    semua_konser = Konser.objects.all()

    return render(request, 'daftar_konser.html', {
        'konser_list': semua_konser
    })


# Detail konser
def detail_konser(request, id):
    konser = get_object_or_404(Konser, id=id)

    return render(request, 'detail_konser.html', {
        'konser': konser
    })


# Kontak
def kontak(request):
    return render(request, 'kontak.html')


# List konser admin
def list_konser(request):
    semua_konser = Konser.objects.all()

    return render(request, 'list.html', {
        'konser_list': semua_konser
    })


# Tambah konser
def tambah_konser(request):
    if request.method == 'POST':
        Konser.objects.create(
            nama_konser=request.POST.get('nama_konser'),
            artis=request.POST.get('artis'),
            lokasi=request.POST.get('lokasi'),
            tanggal=request.POST.get('tanggal'),
            harga_tiket=request.POST.get('harga_tiket'),
            tersedia=request.POST.get('tersedia') == 'on'
        )

        return redirect('list_konser')

    return render(request, 'konser/form.html')