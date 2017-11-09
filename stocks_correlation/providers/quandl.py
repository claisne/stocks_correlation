# -*- coding: utf-8 -*-

"""
stocks_correlation.providers.quandl

This module define how to get a pandas DataFrame
from the Quandl service
"""

import os
import urllib
import pandas as pd

from .pandas import DATAFRAME_COLUMNS
from .exceptions import ProviderError

API_BASE_PATH = 'https://www.quandl.com/api/v3/datasets/WIKI/'

API_KEY_ENV = 'QUANDL_API_KEY'


def url(ticker, start_date, end_date):
    """Format the correct URL from the params"""
    base_url = ''.join([API_BASE_PATH, ticker, '.csv'])

    params = {'start_date': start_date, 'end_date': end_date}
    if API_KEY_ENV in os.environ:
        params['api_key'] = os.environ[API_KEY_ENV]

    return ''.join([base_url, '?', urllib.parse.urlencode(params)])


def dataframe(ticker, start_date, end_date):
    """Build and normalize a DataFrame"""
    csv_url = url(ticker, start_date, end_date)
    try:
        df = pd.read_csv(csv_url)
        df = df[['Date', 'Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close']]
        df.columns = DATAFRAME_COLUMNS
        return df
    except urllib.error.HTTPError as err:
        raise ProviderError('Quandl', ticker, csv_url, err)
