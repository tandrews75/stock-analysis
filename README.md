# stock-analysis
Used to pull and analyze the daily closing stock price for 5000 publicly traded companies

FINANCIAL DISCLAIMER: NOT INVESTMENT ADVICE <br />
I am not a financial advisor. None of the below information should be taken as a form of financial advice or used to make any financial decisions. Any financial decisions made after reading the below information is at the sole discretion of that person and should not be based on any of the information provided on this page. The contents on this site are for informational and entertainment purposes only and does not constitute financial, accounting, or legal advice. I can’t promise that the information shared is appropriate for you or anyone else. By using this site, you agree to hold me harmless from any ramifications, financial or otherwise, that occur to you as a result of acting on information found on this site. This information should not be used in any way to make decisions. 

File breakdown: <br />
|─ main.py                        &nbsp;&nbsp;&nbsp;&nbsp;# Calls all of the individual functions <br />
|─ data_availability.py           &nbsp;&nbsp;&nbsp;&nbsp;# Verifies that you have enough time before the market bell to pull data <br />
|─ raw_yahoo_data_collection.py   &nbsp;&nbsp;&nbsp;&nbsp;# Pulls the Yahoo Finance data for each company and stores in csv files <br />
|─ compile_data.py                &nbsp;&nbsp;&nbsp;&nbsp;# Removes everything except closing price and combines all data into one csv file <br />
|─ create_list_of_company_data.py &nbsp;&nbsp;&nbsp;&nbsp;# Creates pandas dataframe for the closing price data <br />
|─ calculations.py                &nbsp;&nbsp;&nbsp;&nbsp; # Reads in the data and performs basic calculations <br />
|─ README.md <br />

Hypothesis:<br />
The onset of the COVID-19 pandemic created chaos in global financial markets. In February 2020, after reaching all-time highs, the markets experienced an intense sell-off. No companies seemed to be spared from these chaotic market moves. The hypothesis that drove the creation of this program focused on the fact that if there was a market recovery (either through the disappearance of the disease, the development of a vaccine, or human ingenuity allowing society to endure these catastrophic events) it would be an intense and fast recovery. The goal was to identify the companies with: the fastest growth prior to the pandemic-related crash, the largest sell-off during the crash, and quick upticks after the market bottomed out. Identifying the companies that satisfied all of these categories could produce significant returns in the event of a market recovery.

Process: <br />
1) Gather the list of company names and tickers to be analyzed. This list ended up being about 5000 companies from the NYSE and Nasdaq.
2) Pull the financial data from Yahoo Finance using a provided API. The data included in this pull was: daily high, daily low, open price, close price, volume, and adjusted close.
3) Remove all data except for the closing prices and combine all of the data into one file.
4) Transfer that data into a pandas dataframe.
5) Perform calculations on each individual company and then sort all of the companies given the above parameters. The priority was indentifying the companies that were most likley to have the largest potential recovery.<br />
&nbsp;&nbsp;&nbsp;&nbsp; Calculations include:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Finding the maximum before the February crash<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Finding the minimum after the February crash<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Finding the maximum since the February crash<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Finding the low point after the February crash<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Finding the percentage gain between the minimum and maximum after the crash<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Finding the potential gain between current price and the maximum before the crash<br />

6) Combining market knowledge and daily news on companies to figure out which of the highest potential companies were and were not heading towards significant financial troubles.
7) Create a list of companies that could have significant returns.

Output:<br />
Provided below is an example of the formatting for the output produced by this program. Essentially, it sorts all of the company data based on the remaining potential gain that the company could see based on previous highs.

Example: <br />
![image](https://user-images.githubusercontent.com/41634809/129383877-fb09169d-2921-483b-bd42-67840d503d9d.png)

Sucesses: <br />
Below are some of the companies that this program identified as having high returns following the pandemic crash.
![image](https://user-images.githubusercontent.com/41634809/129398540-a113a9c5-91cf-4d85-8eca-b22590738798.png)


Possible Enhancements to the Code:
1) It appears that the Yahoo Finance API that was used for this process is no longer valid. It has either been disconnected or upgraded in a way that requires different calls to the server. An upgraded or new API call would be required to get this up and running agian.
2) The program could be updated to add onto previously compiled data rather than re-pulling all of the data every time it is run. Time was of the essence during this period, but after the fact I dabbled around with this approach. It saves a signficiant amount of time to only have to pull one day's data rather than 1.5 years worth of financial data for 5000 companies.
3) This could be deployed to a server so and run automatically, daily. The reports that are generated could provide users with companies that have possibly been oversold for a certain period of time. This would act similarly to the "biggest losers" page on Yahoo Finance. 



