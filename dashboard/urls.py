from django.urls import path
from dashboard.views import index, manutencao, loginPage, logoutUser, encerrar_manutencao

urlpatterns = [
    path('', index, name='index'),
    path('manutencao/', manutencao, name='manutencao' ),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('encerrar-manutencao/', encerrar_manutencao, name='encerrar-manutencao')
]
