
from pandas_datareader.data import YahooDailyReader
import pandas as pd
import numpy as np
import os
import pandas_datareader as pd_data
from datetime import datetime


def download_stock_daily_csv(tickers, out_dir, start_date, end_date):
    print('len(tickers)', len(tickers))
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    for ticker in tickers:
        file_name = os.path.join(out_dir, ticker + '.csv')
        if os.path.isfile(file_name):
            continue
        try:
            print("Downloading " + ticker)
            df = YahooDailyReader(ticker, start_date, end_date).read()


            df.to_csv(file_name)
        except IOError as error:
            print(error)

start=datetime(2010,1,1)
end=datetime(2017,1,1)
download_stock_daily_csv(['C'], r'C:\Users\cheng\dev\data', start, end)
