from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import response
from rest_framework.response import Response
import requests
from datetime import datetime
import parser
from .serializers import BoardSerializer, CarSerializer
from .models import Car

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars(request):
    return render(request, 'cars.html')

def cars_json(request):
    cars = Car.objects.all()
    return JsonResponse(CarSerializer(cars, many = True).data, safe=False)

def north_station_departure_board_json(request):
    url = 'https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=departure_time&include=schedule%2Cvehicle%2Ctrip&filter%5Bdirection_id%5D=0&filter%5Bstop%5D=place-north'
    informationFromBoardAPI = requests.get(url)
    data_json = informationFromBoardAPI.json()

    allTrainsDict = {}

    for i, data in enumerate(data_json['data']):
        trip_id = data['relationships']['trip']['data']['id']
        schedule_id = data['relationships']['schedule']['data']['id']
        status = data['attributes']['status']

        for include in data_json['included']:
            if include['id'] == trip_id:
                destination = include['attributes']['headsign']
            
        for include in data_json['included']:
            if include['id'] == schedule_id:
                time = str(datetime.strptime(include['attributes']['departure_time'][:19], "%Y-%m-%dT%H:%M:%S").strftime("%-I:%M %p"))
                if len(time) == 7:
                    time = time[:0] + " " + time[0:]

        if data['relationships']['vehicle']['data'] is None:
            trainName = ""
        else:
            vehicle_id = data['relationships']['vehicle']['data']['id']
            for include in data_json['included']: 
                if include['id'] == vehicle_id:
                    trainName = include['attributes']['label']
        
        allTrainsDict['Train' + str(i)] = [time, destination, trainName, status]

    return render(request, 'northstationboard.html', {'allTrainsDict': allTrainsDict.items()})