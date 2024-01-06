# home/views.py

# tambahan 05/01/24
# from django.shortcuts import render, redirect 
from django.contrib import messages
from django.views import View
# from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm



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


# tambahan 05/01/24
def home(request):
    return render(request, 'users/home.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')

        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:

            self.request.session.set_expiry(0)

            self.request.session.modified = True

        return super(CustomLoginView, self).form_valid(form)
    