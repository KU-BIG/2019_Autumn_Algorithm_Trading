import numpy as np
import pandas as pd
import datetime

def make_dataset(df, time_lags=5) :
    df_lag = pd.DataFrame(index=df.index)
    df_lag['Close'] = df['Close']
    df_lag['Volumne'] = df['Volume']
    
    df_lag['Close_Lag%s' % str(time_lags)] = df['Close'].shift(time_lags)
    df_lag['Close_Lag%s_Change' % str(time_lags)] = df_lag['Close_Lag%s' % str(time_lags)].pct_change()*100.0
    
    df_lag['Volumne_Lag%s' % str(time_lags)] = df['Volume'].shift(time_lags)
    df_lag['Volumne_Lag%s_Change' % str(time_lags)] = df_lag['Volumne_Lag%s' % str(time_lags)].pct_change()*100.0
    
    df_lag['Close_Direction'] = np.sign(df_lag['Close_Lag%s_Change' % str(time_lags)])
    df_lag['Volume_Direction'] = np.sign(df_lag['Volumne_Lag%s_Change' % str(time_lags)])
    
    return df_lag.dropna(how='any')

def split_dataset(df, input_column_array, output_column, split_ratio) :
    split_date = get_date_by_percent(df.index[0], df.index[df.shape[0]-1], split_ratio)
    
    x_train = df[input_column_array][df[input_column_array].index < split_date]
    x_test = df[input_column_array][df[input_column_array].index >= split_date]
    y_train = df[output_column][df[output_column].index < split_date]
    y_test = df[output_column][df[output_column].index >= split_date]
    
    return x_train, x_test, y_train, y_test

def get_date_by_percent(start_date, end_date, percent) :
    days = (end_date - start_date).days
    target_days = np.trunc(days * percent)
    target_date = start_date + datetime.timedelta(days=target_days)
    return target_date