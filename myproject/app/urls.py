from django.urls import path
from app.views import *


urlpatterns=[
    path('home/',home,name='home'),
    path('add/',add,name='add'),
    path('complete/',complete,name='complete'),
    path('trash/',trash,name='trash'),
    path('about/',about,name='about'),

    path('delete/<int:pk>',delete_,name='delete'),
    path('completed/<int:pk>',completed,name='completed'),
    path('delete_all/',deleteall,name='delete_all'),

    path('trashdelete/<int:pk>',deletetrash,name='trashdelete'),
    path('deletealltrash',deletealltrash,name='deletealltrash'),
    path('restoretrash/<int:pk>',restoretrash,name='restoretrash'),

    path('deletecomplete/<int:pk>',deletecomplete,name='deletecomplete'),
    path('deleteallcomplete/',deleteallcomplete,name='deleteallcomplete'),
    path('restorecomplete/<int:pk>',resotrecomplete,name='restorecomplete'),

    path('update/<int:pk>',update,name='update'),
    
]