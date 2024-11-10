import requests
from django.shortcuts import render, redirect
import datetime
from main.forms import search_city
from main.models import default_city, search_cityModel




def index(request):

    #appid = '885bcc371445d48240aa552ca0325b64'
    appid = '23c7ce16899544a7906115443240911'
    # url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    url = 'http://api.weatherapi.com/v1/current.json?key={}&q={}&aqi=no' 



    search_list = search_cityModel.objects.all()

    searching_cities = []
    searching_city = {}
    for city in search_list:
        print(city)
    city_info = {}
    searching = "flex"
    if (request.method == 'POST'):
        form = search_city(request.POST)

        if form.is_valid():
            search_res = requests.get(url.format(appid, request.POST['city_name_form'])).json()
            if 'error' in search_res:
                form = search_city()
                searching = "none"
            else:
                form = search_city()
                searching = "flex"
                searching_city = {   
                'city': request.POST['city_name_form'],
                'temp' : int(search_res["current"]["temp_c"]),
                'feels_like' : int(search_res["current"]["feelslike_c"]),
                'icon' : search_res["current"]['condition']["icon"],
                'description' : search_res["current"]['condition']["text"],
                }
                print(searching_city)
                searching_cities.append(searching_city)
    else:
        form = search_city()






    posts = default_city.objects.all()
    default_cities = []

    for city in posts:
        res = requests.get(url.format(appid, city.city_name)).json()
        city_info = {   
            'city': city.city_name,
            'temp' : int(res["current"]["temp_c"]),
            'feels_like' : int(res["current"]["feelslike_c"]),
            'icon' : res["current"]['condition']["icon"],
            'description' : res["current"]['condition']["text"],
        }
        default_cities.append(city_info)

            

    general_info = {
        'time' : datetime.datetime.today().strftime('%H:%M'),
        'date' : datetime.datetime.today().strftime('%d.%m')
    }


    return render(request, 'main/index.html', {'general_info' : general_info, 'default_cities' : default_cities, 'search_state' : searching, "form": form, 'searching_city' : searching_city})


