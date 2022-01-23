"""
#TODO:
    - add error handling
    - envs from config file
"""

import requests
from bs4 import BeautifulSoup
import json
import retry
import pandas as pd

URL_DOMAIN = 'https://www.toronto.ca/'
URL_DIR = 'data/parks/live/locations/centres.json'

# @retry((ValueError, TypeError), delay=1, backoff=2, max_delay=4)


def request_get(url):
    """
    Get the html from a given url.
    """
    response = requests.get(url)
    return response.text


def response_preprocess(response_raw):
    """
    Transform request to standard json
    """

    response_json = json.loads(response_raw)
    return response_json['all']


def response_transform(response_places):
    """
    After getting a response in json of the format:
        {    'ID': 111,
             'Name': 'Evergreen Street',
             'Address': 'string',
             'Phone': 'string',
             'District': 'string',
             'X': 'string',
             'Y': 'string'
        }
    into:
        | ID   | Name       | Address        | Phone | District | X    | Y   |
        ----------------------------------------------------------------------
        |      | Sample     |                | 111   | Sample   |      |     |
        | 111  | Community  | 11 Sample Ave. |  111- | District | -0.0 | 0.0 |
        |      | Centre     |                |  1111 |          |      |     |


    """
    response_datatframe = pd.json_normalize(response_places)
    dtypes = {
        'Name': 'string',
        'Address': 'string',
        'Phone': 'string',
        'District': 'string',
        'X': 'float',
        'Y': 'float'
    }
    return response_datatframe.astype(dtypes)


def get_centres():
    """
    executes the following stages:
        1. create request to toronto data park`s site
        2. data selection (json)
        3. data tranformation to pandas df

    """
    response_raw = request_get(URL_DOMAIN + URL_DIR)
    response_places = response_preprocess(response_raw)
    response_datatframe = response_transform(response_places)
    return response_datatframe


if __name__ == '__main__':
    centres_df = get_centres()
