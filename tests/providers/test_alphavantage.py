# -*- coding: utf-8 -*-
import os
import pytest

from stocks_correlation.providers.alphavantage import url, API_KEY_ENV, dataframe


@pytest.mark.parametrize('ticker, expected', (
    ('MSFT', 'https://www.alphavantage.co/query.csv?function=TIME_SERIES_DAILY_ADJUSTED&outputsize=full&datatype=csv&symbol=MSFT'),
    ('FB', 'https://www.alphavantage.co/query.csv?function=TIME_SERIES_DAILY_ADJUSTED&outputsize=full&datatype=csv&symbol=FB'),
    ('AAPL', 'https://www.alphavantage.co/query.csv?function=TIME_SERIES_DAILY_ADJUSTED&outputsize=full&datatype=csv&symbol=AAPL'),
))
def test_url(ticker, expected):
    api_key = None
    if API_KEY_ENV in os.environ:
        api_key = os.environ[API_KEY_ENV]
        del os.environ[API_KEY_ENV]
    assert url(ticker) == expected
    os.environ[API_KEY_ENV] = api_key


@pytest.mark.parametrize('ticker, start_date, end_date, expected', (
    ('FB', '2017-01-05', '2017-01-05', 'date,open,high,low,close\n2017-01-05,118.86,120.95,118.3209,120.67\n'),
))
def test_dataframe(ticker, start_date, end_date, expected):
    df = dataframe(ticker, start_date, end_date)
    assert df.to_csv(index=False) == expected
