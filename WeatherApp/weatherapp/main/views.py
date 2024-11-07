import requests
from django.shortcuts import render
import datetime




def index(request):
    appid = '885bcc371445d48240aa552ca0325b64'
    url = 'https://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid=' + appid

    city = ''
    london_ = 'london'
    tokyo_ = 'tokyo'
    newyork_ = 'newyork'
    moscow_ = 'moscow'
    paris_ = 'paris'
    dubai_ = 'dubai' 
    rome_ = 'rome'
    res = requests.get(url.format(city)).json()

    london_res = requests.get(url.format(london_)).json()
    tokyo_res = requests.get(url.format(tokyo_)).json()
    newyork_res = requests.get(url.format(newyork_)).json()
    moscow_res = requests.get(url.format(moscow_)).json()
    paris_res = requests.get(url.format(paris_)).json()
    dubai_res = requests.get(url.format(dubai_)).json()
    rome_res = requests.get(url.format(rome_)).json()
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
    city_tokyo = {
        'temp_min' : int(res["main"]["temp_min"]),
        'temp_max' : int(res["main"]["temp_max"]),
        'description' : res["weather"][0]["description"],
    }
    city_newyork = {
        'temp_min' : int(res["main"]["temp_min"]),
        'temp_max' : int(res["main"]["temp_max"]),
        'description' : res["weather"][0]["description"],
    }
    city_moscow = {
        'temp_min' : int(res["main"]["temp_min"]),
        'temp_max' : int(res["main"]["temp_max"]),
        'description' : res["weather"][0]["description"],
    }
    city_paris = {
        'temp_min' : int(res["main"]["temp_min"]),
        'temp_max' : int(res["main"]["temp_max"]),
        'description' : res["weather"][0]["description"],
    }
    city_dubai = {
        'temp_min' : int(res["main"]["temp_min"]),
        'temp_max' : int(res["main"]["temp_max"]),
        'description' : res["weather"][0]["description"],
    }
    city_rome = {
        'temp_min' : int(res["main"]["temp_min"]),
        'temp_max' : int(res["main"]["temp_max"]),
        'description' : res["weather"][0]["description"],
    }
    print(type(city_london["temp_max"]))
    return render(request, 'main/index.html', {'info' : city_info, 'london' : city_london, 'tokyo' : city_london, 'newyork' : city_london, 'moscow' : city_london, 'paris' : city_london, 'dubai' : city_london, 'rome' : city_london})


