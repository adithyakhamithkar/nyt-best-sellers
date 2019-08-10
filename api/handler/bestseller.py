import urllib, json
import logging
from json2html import *


def bestSellerList(API_KEY):
    # variables
    NY_API_URL =  "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=" + API_KEY

    response = urllib.urlopen(NY_API_URL)
    data = json.loads(response.read())
    logging.info('Info: Json data' + str(data))
    html = json2html.convert(json = data)
    return html
