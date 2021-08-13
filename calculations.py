import numpy as numpy
import pandas as pandas
import pickle
from operator import itemgetter


def analyze_data():
    with open('close_prices_list.pickle', "rb") as f:
        closing_prices = pickle.load(f)

    with open('list_of_dates.pickle', 'rb') as f:
        dates = pickle.load(f)

    data_to_analyze = []
    for i in closing_prices:
        data_to_analyze.append(i)

    dates_being_analyzed = 0
    for date in dates:
        if dates[0][:4] == 2020:
            dates_being_analyzed += 1

    # Date of the cash was February 20, 2020
    crash_date = dates.index('2020-02-20')
    crash_date_index_for_companies = crash_date + 2

    # June peak after February 20, 2020 crash
    june_recovery_peak = dates.index('2020-06-08')
    june_recovery_peak_index_for_company = june_recovery_peak + 2

    usable_company_data = []
    total_companies = 0

    for company in data_to_analyze:
        try:
            # Calculate the maximum before the crash
            maximum_before_crash = max(
                company[2:crash_date_index_for_companies])
            index_of_high = company.index(maximum_before_crash)
            # minum since peak but before June recovery high
            minimum_since_peak = min(
                i for i in company[index_of_high:june_recovery_peak_index_for_company] if i > 0)
            index_of_min = company.index(minimum_since_peak)
            # Calculate maximum since minimum
            maximum_since_crash = max(company[index_of_min:])
            index_of_max_since_crash = company.index(maximum_since_crash)

            # Percentage drop from first high to first trough
            percentage_drop_from_peak = (
                maximum_before_crash - minimum_since_peak) / maximum_before_crash
            # calculating the recovery between the lowest drop and June recovery
            percentage_increase_first_recovery = (
                maximum_since_crash - minimum_since_peak) / minimum_since_peak
            # Remaining potential growth
            latest_close = company[-1]
            remaining_potential_gain = (
                maximum_before_crash - latest_close) / latest_close

            # Calculate from beginning of period to before the crash
            # Want to remove anything that has been dropping over time
            growth_direction = (
                company[crash_date_index_for_companies] - company[2]) / company[2]

            if (maximum_before_crash > 0 and minimum_since_peak > 0 and latest_close > 0 and growth_direction < 100000000 and growth_direction >= .1 and remaining_potential_gain > 0.2):
                usable_company_data.append([
                    company[1],                         # 0 company name
                    company[0],                         # 1 company ticker
                    maximum_before_crash,               # 2 company maximum
                    minimum_since_peak,                 # 3 minimum since peak
                    maximum_since_crash,                # 4 recovery since minimum
                    percentage_drop_from_peak,          # 5
                    percentage_increase_first_recovery,  # 6
                    remaining_potential_gain,           # 7
                    latest_close,                       # 8
                    growth_direction,                    # 9
                ])
            total_companies += 1
        except:
            continue

    # Sort all companies in list bsaed on which still have the most to recover

    sorted_companies = sorted(usable_company_data, key=itemgetter(7))

    count = 1
    for company in sorted_companies:
        # print(company[0], company[1], str('{0:.2%}'.format(company[8])))

        if count % 30 == 0:
            print("%-5s %-40s %-15s %-15s %-15s %-15s %-15s %-15s" %
                  ('\n', 'company name',
                         'ticker',
                         'curent value',
                         'maximum',
                         'annual growth',
                         'potential gain',
                         'first recovery'
                   ))

        print("%-5s %-40s %-15s %-15s %-15s %-15s %-15s %-15s" %
              (count,
               company[0],
               company[1],
               '${0:.2f}'.format(company[8]),
               '${0:.2f}'.format(company[2]),
               str('{0:.2%}'.format(company[9])),
               str('{0:.2%}'.format(company[7])),
               str('{0:.2%}'.format(company[6]))
               ))
        count += 1
