# home/urls.py

# tambahan 05/01/24
# from django.urls import path
# from .views import home, RegisterView 

from django.urls import path
from .views import home, RegisterView





    


# urlpatterns = [
#     path('', home, name='users-home'),
# ]

from django.urls import path
from .views import index, mahasiswa_list, add_mahasiswa, edit_mahasiswa, delete_mahasiswa, my_view

urlpatterns = [
    path('', index, name='index'),
    path('my-view/', my_view, name='my_view'),
    path('mahasiswa/', mahasiswa_list, name='mahasiswa_list'),
    path('mahasiswa/add/', add_mahasiswa, name='add_mahasiswa'),
    path('mahasiswa/edit/<int:mahasiswa_id>/', edit_mahasiswa, name='edit_mahasiswa'),
    path('mahasiswa/delete/<int:mahasiswa_id>/', delete_mahasiswa, name='delete_mahasiswa'),

    # tambahan 05/01/24
    # path('admin/', admin.site.urls),
    # path('', include('users.urls')),  
    path('', home, name='users-home'),
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'), 
    # path('register/', RegisterView.as_view(), name='users-register'), 
]
