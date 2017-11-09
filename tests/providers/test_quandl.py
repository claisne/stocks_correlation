# -*- coding: utf-8 -*-
import os
import pytest
import pandas as pd

from stocks_correlation.providers.quandl import url, API_KEY_ENV, dataframe


@pytest.mark.parametrize('ticker, start_date, end_date, expected', (
    ('MSFT', '2010-01-01', '2011-01-01', 'https://www.quandl.com/api/v3/datasets/WIKI/MSFT.csv?start_date=2010-01-01&end_date=2011-01-01'),
    ('FB', '2010-05-27', '2015-07-06', 'https://www.quandl.com/api/v3/datasets/WIKI/FB.csv?start_date=2010-05-27&end_date=2015-07-06'),
    ('AAPL', '2005-10-05', '2008-06-27', 'https://www.quandl.com/api/v3/datasets/WIKI/AAPL.csv?start_date=2005-10-05&end_date=2008-06-27'),
))
def test_url(ticker, start_date, end_date, expected):
    api_key = None
    if API_KEY_ENV in os.environ:
        api_key = os.environ[API_KEY_ENV]
        del os.environ[API_KEY_ENV]
    assert url(ticker, start_date, end_date) == expected
    os.environ[API_KEY_ENV] = api_key


@pytest.mark.parametrize('ticker, start_date, end_date, expected', (
    ('FB', '2017-01-05', '2017-01-05', 'date,open,high,low,close\n2017-01-05,118.86,120.95,118.3209,120.67\n'),
))
def test_dataframe(ticker, start_date, end_date, expected):
    df = dataframe(ticker, start_date, end_date)
    assert df.to_csv(index=False) == expected
