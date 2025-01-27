import requests
API_key = 'd6d51fee81760e1023983e50c890ced5'
city = 'bangkok '
URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}'
#https://api.openweathermap.org/data/2.5/weather?q=bangkok&appid={d6d51fee81760e1023983e50c890ced5}
result = requests.api.get(URL).json()
city_name = result['name']
country = result['sys']['country']
weather = result['weather'][0]['main']
description = result['weather'][0]['description']
temp = result['main']['temp'] - 273.15
print(f'เมือง {city_name} ประะเทศ {country}')
print(f'สภาพอากาศตอนนี้ {weather} โดยมีลักษณะ {description}')
print(f'อุณหภูมิตอนนี้ {temp: .2f} c')
#print(result)