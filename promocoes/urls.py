from django.urls import path
from . import views

app_name = 'promocoes'
urlpatterns = [
    path('', views.index, name='index'), #Lista de promocoes
    path('<int:id>/detail/', views.detail, name='detail'), #Detalhes da promoção
    path('<int:id>/edit/', views.edit, name='edit'), #Editar promoção
    path('new/', views.new, name='new'), #Criar promoção
    path('favoritos/', views.favoritos, name='favoritos'), #Promoções favoritas
    path('favoritar/<int:id>/<str:booleano>/<int:p>/<str:s>', views.favoritar, name='favoritar'), #Promoções favoritas

]