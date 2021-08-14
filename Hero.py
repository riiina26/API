from pprint import pprint
import requests

url = "https://superheroapi.com/api/2619421814940190/"

hero_list_data = ['Hulk', 'Captain America', 'Thanos']
result = {}
def get_data(hero_list):
    for hero in hero_list:
        response = requests.get(url + f'/search/{hero}')
        result[hero] = response.json()
    return result

result = get_data(hero_list_data)
# pprint(result)
iq = {key: value['results'][0]['powerstats']['intelligence'] for key, value in result.items()}
# print(iq)
pprint(sorted(max(iq.items())))
