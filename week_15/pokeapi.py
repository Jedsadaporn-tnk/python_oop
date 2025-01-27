import requests


pokemon_name = 'pikachu'
URL = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'

result = requests.get(URL).json()


name = result['name']
id = result['id']
height = result['height']
weight = result['weight']



print(f'ชื่อโปเกมอน: {name}')
print(f'หมายเลข: {id}')
print(f'ส่วนสูง: {height} dm')
print(f'น้ำหนัก: {weight} hg')

