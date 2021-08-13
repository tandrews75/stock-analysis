# stock-analysis
Used to pull and analyze the daily closing stock price for 5000 publicly traded companies

File breakdown: <br />
|─ main.py                      <t> Calls all of the individual functions <br />
|─ data_availability.py         # Verifies that you have enough time before the market bell to pull data <br />
|─ raw_yahoo_data_collection    # Pulls the Yahoo Finance data for each company and stores in csv files <br />
|─ compile_data                 # Removes everything except closing price and combines all data into one csv file <br />
|─ create_list_of_company_data  # Creates Pandas dataframe for the closing price data <br />
|─ calculations                 # Reads in the data and performs basic calculations <br />
|─ README.md <br />

Hypothesis:<br />

Output:<br />
Provided below is an example of the formatting for the output produced by this program. Essentially, it sorts all of the company data based on the remaining potential gain that the company could see based on previous highs.

Example:
![image](https://user-images.githubusercontent.com/41634809/129383877-fb09169d-2921-483b-bd42-67840d503d9d.png)





