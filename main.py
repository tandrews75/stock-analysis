import datetime as dt
from data_availability import continue_with_data_pull
from raw_yahoo_data_collection import get_raw_yahoo_data
from compile_data import process_one_data_type
from create_list_of_company_data import create_list
# from calculations import analyze_data


def getstockinformation():
    # Check to make sure you have enough time before market bell
    if continue_with_data_pull():
        get_raw_yahoo_data()
    else:
        return

    # If you don't want to do any more processing, you can stop
    proceed_decision = input("Would you like to proceed? (Yes/No): ")
    if proceed_decision:
        process_one_data_type()

    # Create List of company for calculating
    create_list()

    # Perform calculations
    perform_calculations_decision = input(
        "Would you like to perform calculations? (Yes/No): ")
    if perform_calculations_decision == "Yes":
        analyze_data()


if __name__ == "__main__":
    getstockinformation()
