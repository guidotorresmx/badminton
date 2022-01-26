# TODO: paralelize centres extraction

import requests
from bs4 import BeautifulSoup
import json
import retry
import pandas as pd

from general_data_crawler import get_centres

CENTRE_URL = 'https://www.toronto.ca/data/parks/prd/facilities/complex/__route__/index.html'


def data_request_html(centre, id):
    """
    Get html data from specific centre.
    """
    print("data request html " + id)
    url = CENTRE_URL.replace('__route__', id)
    response = requests.get(url)
    return response.text


def data_table_classify(html_table):
    """
    classify tables by insider categories
    """
    if "dropin_General" in html_table:
        return "general"
    elif "dropin_Sports":
        return "sports"


def data_preprocess(html_doc):
    """
    data transform
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    html_tables = soup.find_all(class_="catdropintbl")
    for html_tables_element in html_tables:
        html_tables_element = html_tables_element.find('tr').decompose()
    return html_tables


def data_saver(html_tables, id):
    """
    saves data as html files
    """
    print(id)
    for i, html_table in enumerate(html_tables):
        html_output = html_table.prettify("utf-8")
        print(f"data/output${id}-${i}.html")
        with open(f"data/output${id}-${i}.html", "wb") as file:
            file.write(html_output)


def data_transform_html_to_df(html_tables):
    """
    transform html table to pandas dataframes
        input:

    """
    df_tables = []
    # html_tables[1:] ignores the first element extracted form html tables
    # it creates a multple header table with no useful extra information
    # further investigation may be needed in order to prevent buggy behaviour
    for html_table in html_tables[1:]:
        html_table_str = str(html_table)
        df_tables.append(pd.read_html(html_table_str, displayed_only=False))
    return df_tables


def data_extraction():
    #centres_df = get_centres()
    centres_df = get_centres().tail(1)

    #centre = centres_df.tail(1)
    html_tables = []
    for index, centre in centres_df.iterrows():
        id = str(int(centre['ID']))
        html_raw = data_request_html(centre, id)
        html_tables = data_preprocess(html_raw)
        df_tables = data_transform_html_to_df(html_tables)
        data_saver(html_tables, id)


len(df_tables)
df_tables[1][0]

if __name__ == '__main__':
    data_extraction()


#df_table = data_transform_html_to_df()
