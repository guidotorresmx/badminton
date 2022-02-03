# TODO: delete extra functions and extra dependencies
# TODO: paralelize centres extraction
# get category and week for whole dataframe from config.py
import requests
from bs4 import BeautifulSoup
import json
import retry
import pandas as pd
from datetime import datetime as dt
try:
    from general_data_crawler import get_centres
    from config import search_params
except:
    from models.general_data_crawler import get_centres
    from config import search_params

from loguru import logger
import sys


CENTRE_URL = 'https://www.toronto.ca/data/parks/prd/facilities/complex/__route__/index.html'
CATEGORY = "sports"
ACTIVITY = "badminton"


def data_request_html(centre, id):
    """
    Get html data from specific centre.
    """
    logger.debug("data request html " + id)
    url = CENTRE_URL.replace('__route__', id)
    response = requests.get(url)
    return response.text


def get_table_classification(html_table):
    """
    classify tables by insider categories
    """
    id = html_table.find('tr').get('id')
    if "dropin_" not in id:
        raise Exception("Table name not found", "Unknown activity category")
    category = id.split('_')[1].lower()
    return category


def data_preprocess(html_doc):
    """
    data transform
    """
    #html_doc = html_raw

    soup = BeautifulSoup(html_doc, 'html.parser')

    elements_hr = soup.find_all('hr')
    for element in elements_hr:
        element = element.replace_with(' & ')

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
    df_tables = {}
    for html_table in html_tables:
        table_category = get_table_classification(html_table)
        html_table_str = str(html_table)

        # html_tables[1:] ignores the first element extracted form weekly tables
        # it creates a multple header table with no useful extra information
        # further investigation may be needed in order to prevent buggy behaviour
        weekly_dfs = pd.read_html(html_table_str, displayed_only=False)[1:]
        df_tables[table_category] = weekly_dfs
    return df_tables


def rawdate_to_datetime_array(raw_date_array):
    """
    receives an index array of the format %a %b %d according to
    datetime.datetime.strftime.format_codes, adds current year to datetime
    https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

    """
    def rawdate_to_datetime(datetime_str):
        # date of format 'Sun Jan 23' with no year
        datetime_real = dt.strptime(datetime_str, '%a %b %d')
        day_of_week = datetime_real.weekday()

        datetime_str += ' '
        year_last = str(dt.now().year-1)
        year_curr = str(dt.now().year)
        year_next = str(dt.now().year+1)

        for year in range(dt.now().year-1, dt.now().year+1):
            day_of_week_target = dt.strptime(datetime_str + str(year), '%a %b %d %Y').weekday()
            if day_of_week_target == day_of_week:
                return dt.strptime(datetime_str + str(year), '%a %b %d %Y')
        return dt.strptime(datetime_str + str(year), '%a %b %d %Y')

    datetime_out = [rawdate_to_datetime(datetime_str) for datetime_str in raw_date_array]
    return datetime_out


def get_data():
    # centres_df = get_centres()
    centres_df = get_centres().tail(1)

    html_tables = []
    #centre = centres_df.head(1)
    df_tables = {}
    for index, centre in centres_df.iterrows():
        id = str(int(centre['ID']))
        html_raw = data_request_html(centre, id)
        html_tables = data_preprocess(html_raw)
        df_tables = data_transform_html_to_df(html_tables)
        # data_saver(html_tables, id)

    for index in range(len(df_tables[CATEGORY])):
        columns = df_tables[CATEGORY][index].columns
        columns_dates = columns[1:]
        columns_dates = rawdate_to_datetime_array(columns_dates)
        print(columns_dates)
        df_tables[CATEGORY][index].columns = pd.Index([columns[0]] + columns_dates)
    return df_tables[CATEGORY][0]


if __name__ == '__main__':
    df = get_data()
    df[df['Program'].str.contains(ACTIVITY, case=False)]
