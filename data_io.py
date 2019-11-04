import pandas as pd
import pandas_datareader.data as web
import datetime
import requests
import bs4



def display_all(df) : 
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        display(df)
    return

def download_stock_data(file_name, company_code, year1, month1, date1, year2, month2, date2) :
    start = datetime.datetime(year1, month1, date1)
    end = datetime.datetime(year2, month2, date2)
    df = web.DataReader("%s.KS" % (company_code), "yahoo", start, end)
    
    df.to_csv(file_name)
    
    return df

def load_stock_data(file_name) :
    df = pd.read_pickle(file_name)
    return df

# '퀀트전략 파이썬으로 세워라' 데이터 가공 파트 참조 
# selenium을 이용한 크롤링보다 조금 더 간단하게 진행함

def download_stock_data_from_naver(file_name, symbol, timeframe, count):
    
    #making url
    
    url_a = 'https://fchart.stock.naver.com/sise.nhn?requestType=0'
    url_insert =  url_a+'&symbol='+symbol+'&timeframe='+timeframe+'&count='+count

    #convert into bs(beautifulsoup) object
    
    price_raw = requests.get(url_insert)
    price_bs = bs4.BeautifulSoup(price_raw.text, 'lxml')
    price_list = price_bs.find_all('item')
    
    #empty sheets
    
    date_list = []
    open_list = []
    high_list = []
    low_list = []
    close_list = []
    volume_list = []
    adj_close_list = []
    
    #split the data into date/open/high/low/close/volume
    #close - 차트에서 끌어오기 때문에 수정종가로 자동반영
    
    for piece in price_list:
        temp = piece['data']
        dp = temp.split('|')
        
        date_list.append(dp[0])
        open_list.append(dp[1])
        high_list.append(dp[2])
        low_list.append(dp[3])
        close_list.append(dp[4])
        volume_list.append(dp[5])
        adj_close_list.append('')
    
    #dataframe으로 합치기
    
    dp_to_df = pd.DataFrame({'open': open_list, 'high': high_list, 'low': low_list, 'close': close_list, 'vol': volume_list}, index=date_list)
    
    dp_to_df = pd.DataFrame({'High':high_list,
                            'Low':low_list,
                            'Open':open_list,
                            'Close':close_list,
                            'Volume':volume_list,
                            'Adj Close':adj_close_list}, index=date_list)
    
    dp_to_df.to_csv(file_name)
    
    return dp_to_df
    
def load_data_by_ticker(kospi, ticker) : 
    metadata = kospi[kospi['종목코드'] == ticker]
    
    data = pd.read_pickle('data/kospi/%s.data'%ticker)
    data.index = pd.to_datetime(data.index)
    
    data['High'] = pd.to_numeric(data['High'])
    data['Low'] = pd.to_numeric(data['Low'])
    data['Open'] = pd.to_numeric(data['Open'])
    data['Close'] = pd.to_numeric(data['Close'])
    data['Volume'] = pd.to_numeric(data['Volume'])
    
    return metadata, data

def get_call_data_for_given_ticker(calls, kospi, ticker) : 
    metadata, stock = load_data_by_ticker(kospi, ticker)
    
    # 1. stock
    #display(stock)
    
    # 2. calls
    chicken = calls[calls_amount]
    chicken.index = calls.index
    #display(chicken)
    
    # 3. merge to dataframe to get common period
    df_totest = stock.merge(chicken, how='inner', left_on=stock.index, right_on=chicken.index)
    df_totest.index = df_totest['key_0']
    df_totest = df_totest.drop(['key_0'], axis=1)
    
    return metadata['기업명'].values[0], df_totest