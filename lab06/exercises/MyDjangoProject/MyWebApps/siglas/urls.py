from django.urls import path
from . import views

urlpatterns = [
    # Al entrar a /listar/ se ejecutará la función de la vista
    path('listar/', views.listar_datos, name='listar_datos'),
]