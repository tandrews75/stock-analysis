import datetime as dt
import os
import pickle
import pandas as pd
import pandas_datareader.data as web


def get_raw_yahoo_data():

    start_date = dt.datetime(2019, 1, 1)
    current_time = dt.datetime.now()
    # Import list of NYSE and NASDAQ tickers
    with open('nyse_and_nasdaq_ticker_information.pickle', 'rb') as f:
        list_of_all_companies = pickle.load(f)

    # If no folder exists (first time you're saving in that location) create folder
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    # Data pull should begin from the day after last pull and end with today
    start = start_date + dt.timedelta(days=1)
    end = dt.date.today()

    # Keeping track of the companies found where data was and wasn't found
    list_of_companies_with_no_data = []
    count_company_data_exist = 0
    count_existing_company_new_data = 0
    count_new_company_added = 0
    count_companies_with_no_data = 0

    for company in list_of_all_companies:
        print(company[0], company[1])  # print ticker and company name
        try:
            # If no company data exists in folder then pull all data from specific date
            if not os.path.exists('stock_dfs/{}.csv'.format(company[0])):
                df = web.DataReader(
                    company[0], 'yahoo', dt.datetime(2019, 1, 1), end)
                df.to_csv('stock_dfs/{}.csv'.format(company[0]))
                count_new_company_added += 1
            else:  # otherwise pull data from range and add to existing data
                print('Already have {}'.format(company[0]))
                df = web.DataReader(company[0], 'yahoo', start, end)
                df.to_csv('stock_dfs/_temp.csv')
                # reads the current saved data
                a = pd.read_csv('stock_dfs/{}.csv'.format(company[0]))
                # reads the newly pulled data
                b = pd.read_csv('stock_dfs/_temp.csv')
                # b = b.dropna(axis=1)
                merged = pd.concat([a, b])  # combines the data
                # merged = a.merge(b, on='Date')
                merged.to_csv(
                    'stock_dfs/{}.csv'.format(company[0]), index=False)  # saves the new data
                count_existing_company_new_data += 1
            count_company_data_exist += 1

        except:  # if no company data can be found
            list_of_companies_with_no_data.append(company)
            count_companies_with_no_data += 1
            continue

    # If new data was appended to an old list then remove the temporary file
    if count_existing_company_new_data > 0:
        os.remove('stock_dfs/_temp.csv')

    print("Total number of companies where data exists:", count_company_data_exist)
    print("Total number of companies without data:",
          count_companies_with_no_data)
    print("Number of new companies added to list:", count_new_company_added)
    print("Number of existing companies that new data was added to:",
          count_existing_company_new_data)

    os.remove('dateoflastpull.pickle')
    with open('dateoflastpull.pickle', "wb") as f:
        pickle.dump(current_time, f)
