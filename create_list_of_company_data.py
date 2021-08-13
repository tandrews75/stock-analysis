import pickle
import numpy as np
import pandas as pd


def setdiff_sorted(array1, array2, assume_unique=False):
    ans = np.setdiff1d(array1, array2, assume_unique).tolist()
    if assume_unique:
        return sorted(ans)
    return ans


def create_list():
    # start_date = dt.datetime(2019, 1, 1)

    current_time = dt.datetime.now()

    file_name = 'nyse_nasdaq_closes_{}.csv'.format(current_time.strftime('%d.%m.%Y'))

    # Create a new dataframe of the most recent closing balances
    df = pd.read_csv(file_name, index_col=0)
    df.fillna(0, inplace=True)
    dataframe_tickers = list(df.columns.values)
    list_of_dates = list(df.index.values)

    with open('nyse_and_nasdaq_ticker_information.pickle', "rb") as f:
        company_information = pickle.load(f)

    # Create list of just the tickers
    original_ticker_list = []
    for company in company_information:
        original_ticker_list.append(company[0])

    # Create a list of the missing tickers
    missing_tickers = setdiff_sorted(original_ticker_list, dataframe_tickers)

    total_companies = 0
    closing_prices = []

    with open('stock_dfs/MSFT.csv') as f:
        number_of_days = sum(1 for line in f)

    print(number_of_days)

    # Create a list of all of the company data
    for company in company_information:
        i = 0
        price_list = [company[0], company[1]]
        if company[0] in missing_tickers:
            continue
        else:
            while i < number_of_days:
                try:
                    price_list.append(df[company[0]][i])
                    i += 1
                except:
                    break
            print(price_list)
            closing_prices.append(price_list)
        total_companies += 1

    with open("close_prices_list.pickle", "wb") as f:
        pickle.dump(closing_prices, f)
    print(total_companies)

    with open('list_of_dates.pickle', "wb") as f:
        pickle.dump(list_of_dates, f)
