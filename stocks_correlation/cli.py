# -*- coding: utf-8 -*-

"""
stocks_correlation.providers.cli


This module defines the CLI interface
"""

import datetime
import click
import pandas as pd

from .providers import cli as pcli
from .providers.pandas import CORREL_COMPUTE_COLUMNS

CLI_DATE_FORMAT = '%Y-%m-%d'


def default_start_date():
    """ The default CLI start date, now - 30 days"""
    date = (datetime.datetime.today() + datetime.timedelta(days=-30))
    return date.strftime(CLI_DATE_FORMAT)


def default_end_date():
    """ The default CLI end date, today"""
    date = datetime.datetime.today()
    return date.strftime(CLI_DATE_FORMAT)


@click.command(help='Computes Stocks correlation.')
@click.option(
    '--start-date',
    show_default=True,
    default=default_start_date(),
    help='Start date, format: YYYY-MM-DD'
)
@click.option(
    '--end-date',
    show_default=True,
    default=default_end_date(),
    help='End Date, format: YYYY-MM-DD'
)
@click.option(
    '--value',
    show_default=True,
    default=CORREL_COMPUTE_COLUMNS[0],
    type=click.Choice(CORREL_COMPUTE_COLUMNS),
    help='Value on which correlation is computed'
)
@click.option(
    '--correl-method',
    show_default=True,
    default='pearson',
    type=click.Choice(['pearson', 'kendall', 'spearman']),
    help='Correlation method'
)
@click.option(
    '--provider',
    show_default=True,
    default=pcli.CSV_CHOICE,
    type=click.Choice(pcli.CHOICES),
    help='Data provider'
)
@click.option(
    '--data-save/--no-data-save',
    show_default=True,
    default=False,
    help='Save the data retrieved from providers in the current directory'
)
@click.argument('tickers', nargs=-1)
# Allow a lot of arguments for the cli
# pylint: disable=too-many-arguments
def cli(start_date, end_date, value, correl_method,
        provider, data_save, tickers):
    """Function called when launching the CLI, validates, download and computes
    the stock correlation"""
    if len(tickers) == 0:
        click.echo('You need to specify at least one ticker.')
        click.echo('--help for more info')
        return

    if start_date > end_date:
        click.echo('Start date should not be after end date.')
        click.echo('--help for more info')
        return

    df_by_ticker = pcli.dataframes(provider, tickers, start_date, end_date)

    if data_save:
        for ticker, df in df_by_ticker.items():
            df.to_csv(''.join([ticker, '.csv']))

    dfs_normalized = []
    for ticker, df in df_by_ticker.items():
        df_normalized = df[['date', value]].rename(columns={value: ticker})
        df_normalized = df_normalized.set_index('date')
        dfs_normalized.append(df_normalized)

    df_final = dfs_normalized[0]
    for df_normalized in dfs_normalized[1:]:
        df_final = df_final.join(df_normalized, how='outer')

    df_final = df_final.pct_change()
    print(df_final.corr(method=correl_method))


# pylint does not understand decorators
# pylint: disable=no-value-for-parameter
if __name__ == '__main__':
    cli()
