# -*- coding: utf-8 -*-
import pandas as pd


def get(tickers, start_date, end_date):
    filepath = ''.join([tickers[0], '.csv'])
    df = pd.read_csv(filepath)
    return df
