import json

from django.shortcuts import render
from .forms import WeatherSearch
from geopy.geocoders import Nominatim
import datetime as dt
import meteomatics.api as api


def get_coordinates(city, country):
    try:
        geolocator = Nominatim(user_agent="my_user_agent")
        loc = geolocator.geocode(city + ',' + country)
        return loc.latitude, loc.longitude
    except TypeError:
        return "Not valid city or country!"


def get_weather_info(latitude, longitude):
    username = 'freshairlines_nadzhev'
    password = 'qgkS3N91WK'

    coordinates = [(latitude, longitude)]
    parameters = ['t_2m:C', 'precip_1h:mm']
    model = 'mix'
    start_date = dt.datetime.utcnow().replace(minute=0, second=0, microsecond=0)
    end_date = start_date + dt.timedelta(days=1)
    interval = dt.timedelta(hours=1)

    return api.query_time_series(coordinates, start_date, end_date, interval, parameters, username, password,
                                 model=model).to_json(orient='records')


def weather_search(request):
    context = {
        'valid_info': True,
    }

    if request.method == 'POST':
        form = WeatherSearch(request.POST)
        if form.is_valid():
            city_start = form.cleaned_data['start_city']
            country_start = form.cleaned_data['start_country']
            city_end = form.cleaned_data['end_city']
            country_end = form.cleaned_data['end_country']

            coordinates_start = get_coordinates(city_start, country_start)
            coordinates_end = get_coordinates(city_end, country_end)

            if coordinates_start != "Not valid city or country!" and coordinates_end != "Not valid city or country!":
                weather_start = get_weather_info(coordinates_start[0], coordinates_start[1])
                weather_end = get_weather_info(coordinates_end[0], coordinates_end[1])
                context['location1'] = f"{city_start}, {country_start}"
                context['location2'] = f"{city_end}, {country_end}"
                context['temperature1'] = load_data_in_context(weather_start)
                context['temperature2'] = load_data_in_context(weather_end)
                context['time'] = get_time_24h()
                return render(request, 'weather/weather.html', context)
            else:
                context['valid_info'] = False
    else:
        form = WeatherSearch()

    context['form'] = form
    return render(request, 'weather/weather_search.html', context)


def load_data_in_context(weather_info):
    weather = []
    weather_info = json.loads(weather_info)
    for item in weather_info:
        weather.append(item['t_2m:C'])
    return weather


def get_time_24h():
    start_date = dt.datetime.utcnow().replace(minute=0, second=0, microsecond=0)
    end_date = start_date + dt.timedelta(days=1)

    start_date_str = str(start_date).split(' ')[0]
    start_date_year = str(start_date_str).split('-')[0]
    start_date_month = str(start_date_str).split('-')[1]
    start_date_day = int(str(start_date_str).split('-')[2])
    start_time_hour = int(str(start_date).split(' ')[1].split(':')[0])

    time_window = [str(start_date)]

    while True:
        start_time_hour += 1

        if start_time_hour == 24:
            start_time_hour = 0
            start_date_day += 1

        time_formatted = f'{start_date_year}-{start_date_month}-{str(start_date_day)} {str(start_time_hour)}:00:00'
        time_window.append(time_formatted)

        if len(time_window) == 24:
            break

    return time_window
