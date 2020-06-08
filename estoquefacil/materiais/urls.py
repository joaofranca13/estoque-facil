from django.urls import path
from . import views


app_name = 'materiais'
urlpatterns = [
    path('', views.index, name='index'),
    path('meuestoque/', views.meuestoque, name='meuestoque'),
    path('meuestoque/detalhe/<str:nome>', views.detailview, name='detalhe'),
    path('entrada/', views.entrada, name='entrada')
]
