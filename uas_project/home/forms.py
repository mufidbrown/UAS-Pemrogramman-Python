# home/forms.py

from django import forms
from .models import Mahasiswa

class MahasiswaForm(forms.ModelForm):
    PRODI_CHOICES = [
        ('D3_TEKNIK_INFORMATIKA', 'D3 Teknik Informatika'),
        ('D3_MANAJEMEN_INFORMATIKA', 'D3 Manajemen Informatika'),
        ('TEKNIK_KOMPUTER', 'Teknik Komputer'),
        ('INFORMATIKA', 'Informatika'),
        ('TEKNOLOGI_INFORMASI', 'Teknologi Informasi'),
        ('SISTEM_INFORMASI', 'Sistem Informasi'),
    ]

    ANGKATAN_CHOICES = [(str(year), str(year)) for year in range(2010, 2024)]  # Ganti range sesuai dengan kebutuhan

    nama = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nim = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    prodi = forms.ChoiceField(choices=PRODI_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    angkatan = forms.ChoiceField(choices=ANGKATAN_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Mahasiswa
        fields = ['nama', 'nim', 'prodi', 'angkatan']
