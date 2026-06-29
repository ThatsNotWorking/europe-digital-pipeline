import requests as rq

def get(url):
    response = rq.get(url)

    return response.json()