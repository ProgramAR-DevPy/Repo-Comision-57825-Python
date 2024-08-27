from datetime import datetime as dt

def return_today():
    day = dt.now()
    return day.day

def return_month():
    month = dt.now()
    return month.month

def return_year():
    year = dt.now()
    return year.year