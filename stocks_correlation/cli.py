# -*- coding: utf-8 -*-
import click
import datetime

CLI_DATE_FORMAT = '%Y-%m-%d'


def default_start_date():
    date = datetime.datetime.today()
    return date.strftime(CLI_DATE_FORMAT)


def default_end_date():
    date = (datetime.datetime.today() + datetime.timedelta(days=-30))
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
@click.argument('stocks', nargs=-1)
def cli(start_date, end_date, stocks, correl_method):
    pass


if __name__ == '__main__':
    cli()
