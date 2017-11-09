# -*- coding: utf-8 -*-

"""
stocks_correlation
Init module
"""

from .cli import cli


# pylint does not understand decorators
# pylint: disable=no-value-for-parameter
if __name__ == '__main__':
    cli()
