import datetime as dt
import pickle
import pause


def continue_with_data_pull():
    current_time = dt.datetime.now()
    market_open_time_today = dt.datetime.combine(
        dt.date.today(), dt.time(hour=9, minute=30))
    market_close_time_today = dt.datetime.combine(
        dt.date.today(), dt.time(hour=16, minute=30))

    # Calculate how far you are from open or close in minutes
    time_until_open = ((market_open_time_today - current_time).total_seconds()) / 60
    time_until_close = ((market_close_time_today - current_time).total_seconds()) / 60

    # If you are within 30 minutes of open or close it will tell you to wait
    decision = "Yes"
    time_until_bell = 0
    if 0 < time_until_open < 30:
        decision = input(
            "Wait {} minutes to the bell? (Yes/No):".format(time_until_open))
        time_until_bell = time_until_open
    elif 0 < time_until_close < 30:
        decision = input(
            "Wait {} minutes to the bell? (Yes/No):".format(time_until_close))
        time_until_bell = time_until_close

    if decision == "Yes":
        print("Waiting for {} minutes until the bell.".format(time_until_bell))
        pause.seconds(time_until_bell * 60)
        return True
    else:
        return False
