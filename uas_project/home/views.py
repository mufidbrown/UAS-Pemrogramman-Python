# home/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Mahasiswa
from .forms import MahasiswaForm 
# Assuming you have a MahasiswaForm defined in forms.py
def index(request):
    return render(request, 'home/index.html')

def my_view(request):
    angkatan_choices = range(2010, 2024)  # Sesuaikan dengan kebutuhan
    return render(request, 'home/mahasiswa_list.html', {'angkatan_choices': angkatan_choices})

def mahasiswa_list(request):
    mahasiswa_list = Mahasiswa.objects.all()
    return render(request, 'home/mahasiswa_list.html', {'mahasiswa_list': mahasiswa_list})

def add_mahasiswa(request):
    if request.method == 'POST':
        form = MahasiswaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mahasiswa_list')
    else:
        form = MahasiswaForm()
    return render(request, 'home/add_mahasiswa.html', {'form': form})

def edit_mahasiswa(request, mahasiswa_id):
    mahasiswa = get_object_or_404(Mahasiswa, id=mahasiswa_id)
    if request.method == 'POST':
        form = MahasiswaForm(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            return redirect('mahasiswa_list')
    else:
        form = MahasiswaForm(instance=mahasiswa)
    return render(request, 'home/edit_mahasiswa.html', {'form': form, 'mahasiswa': mahasiswa})

def delete_mahasiswa(request, mahasiswa_id):
    mahasiswa = get_object_or_404(Mahasiswa, id=mahasiswa_id)
    mahasiswa.delete()
    return redirect('mahasiswa_list')
