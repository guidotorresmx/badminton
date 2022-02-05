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


def show_terminal(data, options):
    print(tabulate(data))
    print(data.to_markdown())


def show_powershell(data, options):
    show_terminal(data, options)


def show_web(data, options):
    data.to_html()
