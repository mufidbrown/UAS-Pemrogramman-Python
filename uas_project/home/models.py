# home/models.py

from django.db import models

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=255)
    nim = models.CharField(max_length=20)
    prodi = models.CharField(max_length=50)  # Sesuaikan dengan field yang diinginkan
    angkatan = models.IntegerField()

    def __str__(self):
        return self.nama
