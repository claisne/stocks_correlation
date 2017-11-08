# -*- coding: utf-8 -*-

"""
stocks_correlation.providers.quandl

This module define how to get a pandas DataFrame
from CSV files
"""

import pandas as pd

from .pandas import filter_dates


def dataframe(ticker, start_date, end_date):
    """Build and normalize a DataFrame"""
    filepath = ''.join([ticker, '.csv'])
    df = pd.read_csv(filepath)
    return filter_dates(df, start_date, end_date)
