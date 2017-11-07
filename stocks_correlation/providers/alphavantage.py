# -*- coding: utf-8 -*-
import urllib
import pandas as pd

API_URL = 'https://www.alphavantage.co/query.csv'
API_DEFAULT_PARAMS = {
    'function': 'TIME_SERIES_DAILY',
    'outputsize': 'full',
    'datatype': 'csv',
}


def url(ticker, start_date, end_date):
    params = {**API_DEFAULT_PARAMS, 'symbol': ticker}
    return ''.join([API_URL, '?', urllib.parse.urlencode(params)])


def get(tickers, start_date, end_date):
    df = pd.read_csv(url(tickers[0], start_date, end_date))
    return df
