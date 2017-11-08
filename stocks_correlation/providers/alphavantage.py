# -*- coding: utf-8 -*-

"""
stocks_correlation.providers.alphavantage

This module define how to get a pandas DataFrame
from the Alphavantage service
"""

import urllib
import pandas as pd

from .pandas import DATAFRAME_COLUMNS, filter_dates

API_URL = 'https://www.alphavantage.co/query.csv'
API_DEFAULT_PARAMS = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'outputsize': 'full',
    'datatype': 'csv',
}


def url(ticker):
    """Format the correct URL from the params"""
    params = {**API_DEFAULT_PARAMS, 'symbol': ticker}
    return ''.join([API_URL, '?', urllib.parse.urlencode(params)])


def dataframe(ticker, start_date, end_date):
    """Build and normalize a DataFrame"""
    df = pd.read_csv(url(ticker))
    df = df[['timestamp', 'open', 'high', 'low', 'adjusted_close']]
    df.columns = DATAFRAME_COLUMNS
    return filter_dates(df)
