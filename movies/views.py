from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Film, Jadwal, Studio, Review, Kursi, Tiket
from django.http import JsonResponse
import os
import qrcode
from PIL import Image


def daftar_film(request):
    films = Film.objects.all()
    return render(request, 'daftar_film.html', {'films': films})

from .forms import ReviewForm

def detail_film(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    jadwal = Jadwal.objects.filter(film=film)
    reviews = film.reviews.all() 
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.film = film
            review.save()
            return redirect('detail_film', film_id=film.id) 
    else:
        form = ReviewForm()

    return render(request, 'detail_film.html', {
        'film': film,
        'reviews': reviews,
        'form': form,
        'jadwal' : jadwal
    })

def review_film(request, film_id):
    film = Film.objects.get(id=film_id)
    reviews = Review.objects.filter(film=film)
    
    reviews_with_stars = []
    for review in reviews:
        reviews_with_stars.append({
            'review': review,
            'stars': range(review.rating)
        })
    
    return render(request, 'review_film.html', {'film': film, 'reviews_with_stars': reviews_with_stars})
def sukses(request):
    return render(request, 'sukses.html')

# views.py
def konfirmasi(request, tiket_id):
    tiket = get_object_or_404(Tiket, pk=tiket_id)
    
    # Kirim data tiket ke template konfirmasi
    return render(request, 'konfirmasi.html', {'tiket': tiket})


def pesan_tiket(request, jadwal_id):
    jadwal = get_object_or_404(Jadwal, pk=jadwal_id)
    if request.method == 'POST':
        kursi_ids = request.POST.getlist('kursi')
        kursi_terpilih = Kursi.objects.filter(id__in=kursi_ids, tersedia=True)
        
        if not kursi_terpilih:
            return JsonResponse({'error': 'Kursi tidak tersedia atau sudah dipesan.'})

        kursi_terpilih.update(tersedia=False)

        tiket = Tiket.objects.create(
            jadwal=jadwal,
            jumlah_tiket=len(kursi_terpilih),
        )

        qr_data = f"Tiket ID: {tiket.id}, Kursi: {', '.join(f'{k.baris}{k.nomor}' for k in kursi_terpilih)}"
        qr = qrcode.make(qr_data)

        qr_code_filename = f"tiket_{tiket.id}.png"
        qr_code_path = os.path.join(settings.MEDIA_ROOT, 'qrcodes', qr_code_filename)


        qr.save(qr_code_path)

        kursi_text = ', '.join(f"{k.baris}{k.nomor}" for k in kursi_terpilih)

        return render(request, 'konfirmasi.html', {
            'tiket': tiket,
            'kursi': kursi_text,
            'qr_code_url': f"/media/qrcodes/{qr_code_filename}", 
        })

    kursi_list = Kursi.objects.filter(studio=jadwal.studio).order_by('baris', 'nomor')
    return render(request, 'pilih_kursi.html', {'jadwal': jadwal, 'kursi_list': kursi_list})