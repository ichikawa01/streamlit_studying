import requests
import datetime

API_KEY = 'ddc79cf1bf6f60224b43cbebbc5ac509'

# 緯度、経度
lat = 35.44
lon = 139.44

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
FORECAST_URL = 'http://api.openweathermap.org/data/2.5/forecast'


PARAMS = {
    'q': 'Tokyo,JP',  # 東京都
    'units': 'metric',  # 温度を摂氏で取得
    'appid': API_KEY,
    'lang': 'jp'
}

# PARAMS_FORECAST = {
#     'q': 'Tokyo,JP',  # 東京都
#     'units': 'metric',  # 温度を摂氏で取得
#     'appid': API_KEY
# }




weather_en_to_ja = {
    'Clear':'🌞快晴',
    'Clouds':'☁️曇り',
    'Thunderstorm':'🌩️雷',
    'Drizzle':'🌧️小雨',
    'Rain':'🌧️雨',
    'Snow':'雪',
    'Mist':'🌫️霧',
    'Smoke':'🌫️煙',
    'Haze':'🌫️煙霧',
    'Dust':'🌫️霧',
    'Fog':'🌫️霧',
    'Sand':'砂',
    'Ash':'灰',
    'Squall':'スコール',
    'Tornado':'竜巻',

}


# 確認用
def weather_print():
    # 現在
    response = requests.get(BASE_URL, params=PARAMS)
    data = response.json()

    if response.status_code == 200:
        main_data = data['main']
        weather_data = data['weather'][0]
        # print(f"都市: {data['name']}")
        print(f"気温: {main_data['temp']}℃")
        print(f"最高気温: {main_data['temp_max']}℃")
        print(f"最低気温: {main_data['temp_min']}℃")
        # print(f"気圧: {main_data['pressure']} hPa")
        print(f"湿度: {main_data['humidity']}%")
        print(f"天気: {weather_data['main']}")
    else:
        print(f"エラー: {data['message']}")

    # 予報
    response_fore = requests.get(FORECAST_URL, params=PARAMS)
    data_fore = response_fore.json()
    
    if response_fore.status_code == 200:
        list_data_fore = data_fore['list'][0]
        main_data_fore = list_data_fore['main']
        weather_data_fore = list_data_fore['weather'][0]

        temp_max = -100
        temp_min = 100

        for i in range(4):
            list_tmp = data_fore['list'][i]
            temp_max = max(temp_max,list_tmp['main']['temp_max'])
            temp_min = min(temp_min,list_tmp['main']['temp_min'])

        print('予報')
        # print(list_data_fore['dt'])
        # print(f"気温: {main_data_fore['temp']}℃")
        # print(f"最高気温: {main_data_fore['temp_max']}℃")
        # print(f"最低気温: {main_data_fore['temp_min']}℃")
        
        print(f"最高気温: {temp_max}℃")
        print(f"最低気温: {temp_min}℃")

        print(f"天気: {weather_data_fore['main']}")
    else:
        print(f"エラー: {data['message']}")

def get_now_weather():
    # 現在
    response = requests.get(BASE_URL, params=PARAMS)
    data = response.json()

    if response.status_code == 200:
        main_data = data['main']
        weather_data = data['weather'][0]
        # print(f"都市: {data['name']}")
        now_temp = main_data['temp']
        now_max_temp = main_data['temp_max']
        now_min_temp = main_data['temp_min']
        now_humidity = str(main_data['humidity'])
        now_weather = weather_data['main']

        return [now_temp,now_max_temp,now_min_temp,now_humidity,weather_en_to_ja[now_weather]]

def get_for_weather():
    # 予報
    response_fore = requests.get(FORECAST_URL, params=PARAMS)
    data_fore = response_fore.json()
    
    if response_fore.status_code == 200:
        list_data_fore = data_fore['list'][0]
        # main_data_fore = list_data_fore['main']
        weather_data_fore = list_data_fore['weather'][0]

        temp_max = -100
        temp_min = 100

        for i in range(4):
            list_tmp = data_fore['list'][i]
            temp_max = max(temp_max,list_tmp['main']['temp_max'])
            temp_min = min(temp_min,list_tmp['main']['temp_min'])

        for_max_temp = temp_max
        for_min_temp = temp_min
        for_weather = weather_data_fore['main']

        return [for_max_temp,for_min_temp,weather_en_to_ja[for_weather]]

