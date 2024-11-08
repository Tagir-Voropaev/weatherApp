import requests
from django.shortcuts import render
import datetime
import psycopg2





def index(request):
    
    appid = '885bcc371445d48240aa552ca0325b64'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid


   
       

    general_info = {
        'time' : datetime.datetime.today().strftime('%H:%M'),
        'date' : datetime.datetime.today().strftime('%d.%m')
    }

    city = "london"
    res = requests.get(url.format(city)).json()


    city_info = {
        'city': city,
        'temp' : int(res["main"]["temp"]),
        'feels_like' : res["main"]["feels_like"],
        'icon' : res["weather"][0]["icon"],
        'temp_min' : int(res["main"]["temp_min"]),
        'temp_max' : int(res["main"]["temp_max"]),
        'description' : res["weather"][0]["description"],
        'error': False  
    }


    
    

    
    if (city_info['temp_max'] > 0):
        city_info['temp_max'] = "+" + str(city_info['temp_max'])
    elif(city_info['temp_max'] < 0):
        city_info['temp_max'] = "-" + str(city_info['temp_max'])
    else:
        city_info['temp_max'] = "" + str(city_info['temp_max'])

    if (city_info['temp_min'] > 0):
        city_info['temp_min'] = "+" + str(city_info['temp_min'])
    elif(city_info['temp_min'] < 0):
        city_info['temp_min'] = "-" + str(city_info['temp_min'])
    else:
        city_info['temp_min'] = "" + str(city_info['temp_min'])
    

    return render(request, 'main/index.html', {'general_info' : general_info})


