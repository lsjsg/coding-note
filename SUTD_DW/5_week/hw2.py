# NB: the following line imports the 'display_calendar', 'lear_year', etc. functions
# (see the problem sheet PDF)
# DO NOT delete hw2_others.pyc from Vocareum :-)
from hw2_others import *

# You should ONLY submit the 'display_calendar_modified' function

def display_calendar_modified(year, month=None):
    if month==None:
        return display_calendar(year)
    elif 0<month<13:
        string = construct_cal_year(year)[month][0] + "\n  S  M  T  W  T  F  S\n"
        for i in construct_cal_year(year)[month][1:]:
            string += i + "\n"
        return string[:-1]
