# -*- coding: utf-8 -*-
import click
import datetime

from . import providers

CLI_DATE_FORMAT = '%Y-%m-%d'


def default_start_date():
    date = (datetime.datetime.today() + datetime.timedelta(days=-30))
    return date.strftime(CLI_DATE_FORMAT)


def default_end_date():
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
        '--correl-method',
        show_default=True,
        default='pearson',
        type=click.Choice(['pearson', 'kendall', 'spearman']),
        help='Correlation method'
)
@click.option(
        '--provider',
        show_default=True,
        default=providers.CSV_CHOICE,
        type=click.Choice(providers.CHOICES),
        help='Data provider'
)
@click.option(
        '--data-save/--no-data-save',
        default=False,
        show_default=True,
        help='Save the data retrieved from providers in the current directory'
)
@click.argument('tickers', nargs=-1)
def cli(start_date, end_date, tickers, correl_method, provider, data_save):
    dfs = providers.dataframes(provider, tickers, start_date, end_date)

    if data_save:
        for df in dfs:
            df.to_csv(''.join([tickers[0], '.csv']), index=False)

    for df in dfs:
        print(df.head())


if __name__ == '__main__':
    cli()
