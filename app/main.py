from imdbpie import ImdbFacade, Imdb

from typing import Optional
from fastapi import FastAPI
from starlette.requests import Request
from justwatch import JustWatch
import os
import logging

app = FastAPI()
logger = logging.getLogger("fastapi")
logger.setLevel(logging.DEBUG)

imdb = Imdb()
just_watch = JustWatch(country='US')


@app.get("/")
def read_root():
    return {"Go": "Away"}


@app.get("/title/{item_id}")
def get_title(item_id: str):
    val = imdb.get_title(imdb_id=item_id)
    return {"title": val}


@app.get("/title_search/{query}")
def search_title(query: str, request: Request):
    results = []
    base = request.url.scheme + '://' + \
        request.url.hostname
    if request.url.port != None:
        base = base + ':' + str(request.url.port)

    titles = imdb.search_for_title(query)
    for p in titles:
        results.append({
            'id': p['imdb_id'],
            'title': p['title'],
            'link': base + '/title/' + p['imdb_id'],
            'type': p['type'],
            'year': p['year']
        })
    return results


@app.get("/popular_movies")
def popular_movies(request: Request):
    results = []
    base = request.url.scheme + '://' + \
        request.url.hostname
    if request.url.port != None:
        base = base + ':' + str(request.url.port)
    popular = imdb.get_popular_movies()
    for p in popular["ranks"]:
        results.append({
            'id': p['id'],
            'title': p['title'],
            'link': base + '/title/' + p['id'],
            'type': p['titleType'],
            'year': p['year']
        })
    return results


@app.get("/name/{name_id}")
def get_name(name_id: str):
    result = imdb.get_name(imdb_id=name_id)
    return result


@app.get("/name/{name_id}/images")
def get_name_images(name_id: str):
    images = imdb.get_name_images(imdb_id=name_id)
    return images


@app.get("/name/{name_id}/images/{image_id}")
def get_name_image(name_id: str, image_id: str):
    result = {}
    images = imdb.get_name_images(imdb_id=name_id)
    for p in images['images']:
        if p['id'].endswith(image_id):
            result = p
    return result


@app.get("/name_search/{query}")
def search_title(query: str, request: Request):
    results = []
    base = request.url.scheme + '://' + \
        request.url.hostname + ':' + str(request.url.port)
    names = imdb.search_for_name(query)
    for p in names:
        results.append({
            'id': p['imdb_id'],
            'link': base + '/name/' + p['imdb_id'],
            'name': p['name']
        })
    return results


@app.get("/streaming/providers")
def justwatch_providers(request: Request):
    provider_details = just_watch.get_providers()
    return provider_details


@app.get("/streaming/{query}")
def justwatch_query(query: str, request: Request):
    results = just_watch.search_for_item(query=query)
    return results
