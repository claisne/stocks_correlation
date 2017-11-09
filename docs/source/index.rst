.. stocks_correlation documentation master file, created by
   sphinx-quickstart on Mon Nov  6 19:15:12 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

stocks_correlation
==============================================

**stocks_correlation** is a CLI tool which let you
compute correlation between stocks.

As a starter, here is an output of the help from the CLI::

  Computes Stocks correlation. Available data providers are csv, quandl,
  alphavantage. The correlation can be computed on the open, low, high and
  close values of the stocks. Some providers require an API key, that you
  can retrieve online (check the documentation for more information on
  available providers). The --save flag will dump all the data retrieved
  from the providers in the current directory as CSVs.

  Options:
  --start-date TEXT               Start date, format: YYYY-MM-DD  [default:
                                  2017-10-10]
  --end-date TEXT                 End Date, format: YYYY-MM-DD  [default:
                                  2017-11-09]
  --value [open|high|low|close]   Value on which correlation is computed
                                  [default: close]
  --correl-method [pearson|kendall|spearman]
                                  Correlation method  [default: pearson]
  --provider [csv|quandl|alphavantage]
                                  Data provider  [default: csv]
  --save / --no-save              Save the data retrieved from providers in
                                  the current directory  [default: False]
  --help                          Show this message and exit.


Available Providers
-------------------

Quandl
^^^^^^
Stocks are retrieved from the WIKI dataset which is free, and created and
maintained by its community. This dataset is free of access, but you may
hit the limits of usage (50 calls per day). in this case, create an account
and retrieve your API key. before executing stocks_correlation again, set
the environment variable QUANDL_API_KEY to your API key.

Alphavantage
^^^^^^^^^^^^

Alphavantage is another free service to retrieve data stocks. However you must
have an API key. Retrieve it on their website.

CSV
^^^

This provider reads for each tickers you write the {ticker}.csv file. You can use
this provider in combination of the previous providers and the --save flag
