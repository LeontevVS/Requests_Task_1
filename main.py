import requests


path = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url=path)
heroes = dict.fromkeys(["Hulk", "Captain America", "Thanos"])
all_heroes = response.json()
info = list(filter(lambda x: x['name'] in heroes, all_heroes))
for hero in info:
    heroes[hero['name']] = hero['powerstats']['intelligence']
heroes = list(heroes.items())
smartest = max(heroes, key=lambda x: x[1])
print(smartest[0])