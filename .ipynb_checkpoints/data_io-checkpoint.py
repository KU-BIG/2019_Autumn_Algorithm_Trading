import pandas as pd
import pandas_datareader.data as web
import datetime

def download_stock_data(file_name, company_code, year1, month1, date1, year2, month2, date2) :
    start = datetime.datetime(year1, month1, date1)
    end = datetime.datetime(year2, month2, date2)
    df = web.DataReader("%s.KS" % (company_code), "yahoo", start, end)
    
    df.to_pickle(file_name)
    
    return df

def load_stock_data(file_name) :
    df = pd.read_pickle(file_name)
    return df