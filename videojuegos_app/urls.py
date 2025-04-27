from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar_desarrollador/', views.agregar_desarrollador, name='agregar_desarrollador'),
    path('agregar_plataforma/', views.agregar_plataforma, name='agregar_plataforma'),
    path('agregar_videojuego/', views.agregar_videojuego, name='agregar_videojuego'),
    path('buscar/', views.buscar_videojuego, name='buscar_videojuego'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
