from django.db import models

class Film(models.Model):
    judul = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    durasi = models.PositiveIntegerField() 
    sinopsis = models.TextField()
    poster = models.ImageField(upload_to='film_posters/')
    
    def __str__(self):
        return self.judul
    
class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='reviews')
    pengguna = models.CharField(max_length=255)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    komentar = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)
   


class Studio(models.Model):
    TIPE_CHOICES = [
        ('VIP', 'VIP'),
        ('Deluxe', 'Deluxe'),
        ('Biasa', 'Biasa'),
    ]
    
    nama = models.CharField(max_length=100)
    tipe = models.CharField(max_length=10, choices=TIPE_CHOICES, default='Biasa')
    
    def get_capacity(self):
        if self.tipe == 'VIP':
            return 20
        elif self.tipe == 'Deluxe':
            return 30
        else:
            return 50 

    @property
    def kapasitas(self):
        return self.get_capacity()

    def __str__(self):
        return self.nama


class Jadwal(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    waktu_tayang = models.DateTimeField()

    def __str__(self):
        return f"{self.film.judul} - {self.waktu_tayang}"

class Kursi(models.Model):
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    baris = models.CharField(max_length=1) 
    nomor = models.PositiveIntegerField()  
    tersedia = models.BooleanField(default=True)

    class Meta:
        unique_together = ('studio', 'baris', 'nomor')  

    def __str__(self):
        return f"{self.baris}{self.nomor} - {self.studio.nama}"

class Tiket(models.Model):
    jadwal = models.ForeignKey(Jadwal, on_delete=models.CASCADE)
    kursi = models.ManyToManyField(Kursi) 
    jumlah_tiket = models.PositiveIntegerField()
    waktu_pemesanan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tiket untuk {self.jadwal.film.judul} ({self.jumlah_tiket} kursi)"