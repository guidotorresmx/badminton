from data.data import data
from loguru import logger
from config import show_options
from tabulate import tabulate


def show_data(data, options):
    if show_options.terminal:
        show_terminal(data, options)
    if show_options.powershell:
        show_powershell(data, options)
    if show_options.web:
        show_web(data, options)
    if show_options.excel:
        show_excel(data, options)


def show_terminal(data):
    print(tabulate(df))
    print(df.to_markdown())
