import requests
from django.shortcuts import render
import datetime




def index(request):
    appid = '885bcc371445d48240aa552ca0325b64'
    url = 'https://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid=' + appid

    city = ''
    london_ = 'london'
    
    res = requests.get(url.format(city)).json()

    london_res = requests.get(url.format(london_)).json()

    city_info = {
        'city': city,
        'temp' : res["main"]["temp"],
        'feels_like' : res["main"]["feels_like"],
        'icon' : res["weather"][0]["icon"],
        'temp_min' : res["main"]["temp_min"],
        'temp_max' : res["main"]["temp_max"],
        'description' : res["weather"][0]["description"],
        'time' : datetime.datetime.today().strftime('%H:%M'),
        'date' : datetime.datetime.today().strftime('%d.%m')
    }
    city_london = {
        'temp_min' : int(res["main"]["temp_min"]),
        'temp_max' : int(res["main"]["temp_max"]),
        'description' : res["weather"][0]["description"],
    }
   
    return render(request, 'main/index.html', {'info' : city_info, 'london' : city_london})


