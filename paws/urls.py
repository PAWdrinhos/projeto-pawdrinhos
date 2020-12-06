"""pawdrinhos URL Configuration"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio, name='inicio'),
    path('signin/', views.Sign, name='logar'),
    path('signup/', views.Cad, name='cadastrar'),
    path('padrinho/', views.Home, name='home-padrinho'),
    path('logout/', views.Logout, name="logout"),
    path('ong/', views.HomeOng, name='home-ong'),
    path('padrinho/profile/', views.pProfile, name='profile-padrinho'),
    path('padrinho/ong/<int:ong>/', views.getOng, name="view-ong"),
    path('padrinho/ong/apadrinhar/<int:paw>', views.Apadrinhar, name='view-apadrinhar'),
    path('ong/profile/', views.pOng, name="ong-profile"),
    path('ong/padrinho/<int:padrinho>/', views.getPadrinho, name="view-padrinho"),
]
