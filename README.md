# stock-analysis
Used to pull and analyze the daily closing stock price for 5000 publicly traded companies

|─ main.py  # Run the main program that calls all of the individual functions <br />
|─ data_availability.py  # Verifies that you have enough time before the market bell to pull all of the data <br />
|─ raw_yahoo_data_collection # Pulls the Yahoo Finance data for each company and individual company data in csv files with ticker as filename <br />
|─ compile_data  # Removes all data except daily stock closing price and combines all data into one csv file <br />
|─ create_list_of_company_data # Creates Pandas dataframe for the closing price data and stores in a .pickle file <br />
|─ calculations #Reads in the data and performs basic calculations <br />
|─ README.md <br />



