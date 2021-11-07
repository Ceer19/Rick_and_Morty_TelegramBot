import requests
import json
import random
from param_and_send_to import processing, random_params


def random_pers():
    url = f"https://rickandmortyapi.com/api/character/{random.randint(1, 183)}"
    response = requests.request("GET", url)
    return random_params(response)


def search(search_person):
    url2 = f"https://rickandmortyapi.com/api/character/?name={search_person}"
    response = requests.request("GET", url2)
    return processing(response)



