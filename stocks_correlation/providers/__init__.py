# -*- coding: utf-8 -*-
from . import csv
from . import quandl
from . import alphavantage

CSV_CHOICE = 'csv'
QUANDL_CHOICE = 'quandl'
ALPHAVANTAGE_CHOICE = 'alphavantage'

PROVIDER_BY_CHOICE = {
        CSV_CHOICE: csv.get,
        QUANDL_CHOICE: quandl.get,
        ALPHAVANTAGE_CHOICE: alphavantage.get,
}

CHOICES = PROVIDER_BY_CHOICE.keys()


def from_choice(choice):
    return PROVIDER_BY_CHOICE[choice]


def dataframes(choice, tickers, start_date, end_date):
    get = from_choice(choice)
    return [get(ticker, start_date, end_date) for ticker in tickers]
