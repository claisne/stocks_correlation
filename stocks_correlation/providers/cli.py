# -*- coding: utf-8 -*-

"""
stocks_correlation.providers.cli

This module define convenience functions to build the CLI
"""

from . import csv
from . import quandl
from . import alphavantage

CSV_CHOICE = 'csv'
QUANDL_CHOICE = 'quandl'
ALPHAVANTAGE_CHOICE = 'alphavantage'

PROVIDER_BY_CHOICE = {
    CSV_CHOICE: csv.dataframe,
    QUANDL_CHOICE: quandl.dataframe,
    ALPHAVANTAGE_CHOICE: alphavantage.dataframe,
}

CHOICES = PROVIDER_BY_CHOICE.keys()


def from_choice(choice):
    """Returns the correct provider funtion from a CLI choice"""
    return PROVIDER_BY_CHOICE[choice]


def dataframes(choice, tickers, start, end):
    """Return a normalized DataFrame from CLI params"""
    dataframe = from_choice(choice)
    return {ticker: dataframe(ticker, start, end) for ticker in tickers}
