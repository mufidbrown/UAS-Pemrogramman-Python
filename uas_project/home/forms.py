# home/forms.py

# tambahan 05/01/24
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



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



# tambahan 05/01/24
class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
