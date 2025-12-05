from django.urls import path
from authapp.views import *

urlpatterns=[
    path('register/',register,name='register'),
    path('login/',authlogin,name='login'),
    path('logout/',authlogout,name='logout')
]