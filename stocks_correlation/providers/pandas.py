# -*- coding: utf-8 -*-

"""
stocks_correlation.providers.quandl

This module define the normalized columns
of the DataFrame the providers return
"""

DATAFRAME_COLUMNS = ['date', 'open', 'high', 'low', 'close']
CORREL_COMPUTE_COLUMNS = DATAFRAME_COLUMNS[1:]


def filter_dates(df, start_date, end_date):
    """Filters the DataFrame so that all ticks are
    between start_date and end_date"""
    return df[(df['date'] >= start_date) & (df['date'] <= end_date)]
