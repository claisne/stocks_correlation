# -*- coding: utf-8 -*-

"""
stocks_correlation.providers.exceptions

This module define providers exceptions
"""


class ProviderError(Exception):
    """Exception which provides a formated error message"""
    def __init__(self, provider, ticker, url, error):
        ticker_line = "Ticker: {}".format(ticker)
        provider_line = "Provider: {}".format(provider)
        url_line = "Url: {}".format(url)
        error_line = "Exception: {}".format(repr(error))

        message = '\n'.join([
            'Failed to build the DataFrame.'
            'Check the URL for more information.',
            ticker_line,
            provider_line,
            url_line,
            error_line,
        ])

        super(ProviderError, self).__init__(message)
