# -*- coding: utf-8 -*-

"""
stocks_correlation.providers.alphavantage

This module define how to get a pandas DataFrame
from the Alphavantage service
"""

import os
import urllib
import pandas as pd

from .pandas import DATAFRAME_COLUMNS, filter_dates
from .exceptions import ProviderError

API_URL = 'https://www.alphavantage.co/query.csv'

API_DEFAULT_PARAMS = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'outputsize': 'full',
    'datatype': 'csv',
}

API_KEY_ENV = 'ALPHAVANTAGE_API_KEY'


def url(ticker):
    """Format the correct URL from the params"""
    params = {**API_DEFAULT_PARAMS, 'symbol': ticker}
    if API_KEY_ENV in os.environ:
        params['apikey'] = os.environ[API_KEY_ENV]

    return ''.join([API_URL, '?', urllib.parse.urlencode(params)])


def dataframe(ticker, start_date, end_date):
    """Build and normalize a DataFrame"""
    csv_url = url(ticker)
    try:
        df = pd.read_csv(csv_url)
        df = df[['timestamp', 'open', 'high', 'low', 'adjusted_close']]
        df.columns = DATAFRAME_COLUMNS
        return filter_dates(df, start_date, end_date)
    except Exception as err:
        raise ProviderError('Alphavantage', ticker, csv_url, err)
