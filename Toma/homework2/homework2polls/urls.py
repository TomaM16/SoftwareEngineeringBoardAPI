from django.urls import include, path
from homework2polls import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('about', views.about),
    path('api/v1/cars', views.cars_json),
    path('api/v1/northstationboard', views.north_station_departure_board_json),
]
