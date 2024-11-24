from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_film, name='daftar_film'),
    path('film/<int:film_id>/', views.detail_film, name='detail_film'),
    path('review/<int:film_id>/', views.review_film, name='review_film'),
    path('pesan_tiket/<int:jadwal_id>/', views.pesan_tiket, name='pesan_tiket'),
    path('konfirmasi/<int:tiket_id>/', views.konfirmasi, name='konfirmasi'),


]
