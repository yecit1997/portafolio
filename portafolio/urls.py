from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('sobremi/', sobre_mi, name='sobremi'),
    path('ver_proyecto/<int:proyecto_id>/', ver_proyecto, name='ver_proyecto'),
]
