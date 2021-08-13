import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests


def process_one_data_type():
    with open('nyse_and_nasdaq_ticker_information.pickle', "rb") as f:
        tickers = pickle.load(f)

    data_type_selection = "Close"

    # Create dataframe to store data
    main_df = pd.DataFrame()
    duplicate_ticker_check = []

    # Create a list of all data types not reviewing so we can remove them from raw data
    list_of_not_selected_data_options = ['High', 'Low',
                                         'Open', 'Close', 'Volume', 'Adj Close']
    list_of_not_selected_data_options.remove(data_type_selection)

    print(data_type_selection)
    print("List to delete", list_of_not_selected_data_options)

    for count, ticker in enumerate(tickers):
        try:
            # if the ticker has already been added then ignore duplicates and skip
            if ticker[0] in duplicate_ticker_check:
                continue

            # add the new ticker to the list of tickers that have already been reviewed
            duplicate_ticker_check.append(ticker[0])

            # Add the date, ticker, and data to the dataframe
            df = pd.read_csv('stock_dfs/{}.csv'.format(ticker[0]))
            df.set_index('Date', inplace=True)
            df.rename(columns={data_type_selection: ticker[0]}, inplace=True)
            df.drop(list_of_not_selected_data_options, 1, inplace=True)

        except:
            continue

        if main_df.empty:
            main_df = df
        else:
            # Let us have information from both so that we dont lose data
            main_df = main_df.join(df, how='outer')

        if count % 10 == 0:
            print(count)

    print(main_df.head())
    print("................")
    print(main_df.tail())

    main_df.to_csv('nyse_nasdaq_closes_{}.csv'.format(
        dt.date.today().strftime('%d.%m.%Y')))
