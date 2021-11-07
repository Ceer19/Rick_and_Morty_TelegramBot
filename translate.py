import requests
import json
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
token = config['Token_AB']['token']
headers = {
  'Authorization': token
}


def translate(trans_word):
    url = f"https://developers.lingvolive.com/api/v1/Minicard?text={trans_word}&srcLang=1033&dstLang=1049"
    response = requests.request("GET", url, headers=headers)
    try:
        text = str(response.json()["Translation"]["Translation"])
        return str(text.split(", ")[0].split(" ")[0].replace(";", "").capitalize())
    except:
        return "The transfer failed"



