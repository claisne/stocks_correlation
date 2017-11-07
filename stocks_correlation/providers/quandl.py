# -*- coding: utf-8 -*-
import urllib
import pandas as pd

API_BASE_PATH = 'https://www.quandl.com/api/v3/datasets/WIKI/'


def url(ticker, start_date, end_date):
    url = ''.join([API_BASE_PATH, ticker, '.csv'])
    params = {'start_date': start_date, 'end_date': end_date}
    return ''.join([url, '?', urllib.parse.urlencode(params)])


def get(tickers, start_date, end_date):
    df = pd.read_csv(url(tickers[0], start_date, end_date))
    df = df[['Date', 'Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close']]
    df.columns = ['date', 'adj.open', 'adj.high', 'adj.low', 'adj.close']
    return df
