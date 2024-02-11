# weather/views.py
from django.shortcuts import render
import requests

def weather_view(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = '55d42c1ea820eb0271ff79c3a1aeb8f7'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        print("my data "+str(data))
        context = {
            'city': city,
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }

        return render(request, 'weather.html', context)

    return render(request, 'weather.html')