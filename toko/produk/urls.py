from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('konser/', views.daftar_konser, name='konser'),
    path('konser/<int:id>/', views.detail_konser, name='detail_konser'),

    path('admin/konser/', views.list_konser, name='list_konser'),
    path('admin/konser/tambah/', views.tambah_konser, name='tambah_konser'),

    path('kontak/', views.kontak, name='kontak'),
]