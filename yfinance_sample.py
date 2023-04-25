# https://pypi.org/project/yfinance/
# https://finance.yahoo.com/world-indices

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from typing import Union
from pandas.tseries.offsets import MonthEnd, YearEnd, QuarterEnd
from dateutil.relativedelta import relativedelta, FR

from data_sources import equity_indices

def calc_cumu_returns(returns: pd.DataFrame) -> pd.DataFrame: 
    ''''''
    return (1 + returns).cumprod() - 1


def calc_total_returns(returns: pd.DataFrame) -> pd.DataFrame: 
    return (1 + returns).prod() - 1


def calc_period_returns(
    returns: pd.DataFrame, start_date: str, end_date: str,
    cumu_flag: bool = False) -> Union[pd.DataFrame, pd.Series]: 
    
    fn = calc_cumu_returns if cumu_flag else calc_total_returns
    return fn(returns.copy().loc[start_date:end_date])


def calc_perf_intervals(end_date: str) -> dict[str, list[str, str]]: 
    
    # print(end_date + relativedelta(weekday=FR(-1)))
    # print(end_date - relativedelta(weekday=FR(1)))
    
    return {
        'one_day': [end_date - timedelta(1), end_date],
        'one_week': [end_date - timedelta(7), end_date], 
        'one_month': [end_date - timedelta(30), end_date], 
        'three_month': [end_date - timedelta(91), end_date], 
        'six_month': [end_date - timedelta(182), end_date],
        'one_year': [end_date - timedelta(365), end_date], 
        # 'three_year': [end_date - timedelta(365*3), end_date], 
        # 'five_year': [end_date - timedelta(365*5), end_date], 
        'week_to_date': [end_date + relativedelta(weekday=FR(-1)), end_date],
        'month_to_date': [end_date - MonthEnd(1), end_date], 
        'quarter_to_date': [end_date - QuarterEnd(1), end_date],
        'year_to_date': [end_date - YearEnd(1), end_date]
    }

def main() -> None: 
    end_date = datetime.today() - timedelta(1) # yesterday's close date
    start_date = end_date - timedelta(365*5)

    close_price = pd.DataFrame(index=pd.bdate_range(start=start_date, end=end_date))

    for _, ticker in equity_indices.items(): 
        
        idx = yf.Ticker(ticker)
        ts = idx.history('1y')
        
        ts.index = ts.index.tz_localize(None)
        ts.rename(columns={'Close': ticker}, inplace=True)
        close_price = pd.merge(
            left=close_price, 
            right=ts[ticker],
            left_index=True, 
            right_index=True, 
            how='left' 
        )

    returns = close_price.fillna(method='ffill').dropna().pct_change()
    # print(min(returns.index))
    # cumu_returns = calc_cumu_returns(returns)

    interval_dates = calc_perf_intervals(end_date=end_date)

    perf_table = pd.DataFrame()
    for period, dates in interval_dates.items(): 
        int_returns = calc_period_returns(
            returns=returns, 
            start_date=dates[0], 
            end_date=dates[1], 
            cumu_flag=False)
        perf_table[period] = int_returns
        print(f'{period}: {dates[0]}-{dates[1]}')
        # int_returns.plot(kind='bar', title=f'{period}: {dates[0]}-{dates[1]}')
        # plt.show()

    print(perf_table)
    
    # bar chart
    # perf_table.T.plot(kind='bar', stacked=False, title='Performance Table')
    # plt.grid(axis='y', alpha=0.5)
    # plt.show()

    # heat map
    # sns.heatmap(perf_table*100, annot=True)#, cbar_ax=1)
    # plt.show()

if __name__ == '__main__': 
    main()

