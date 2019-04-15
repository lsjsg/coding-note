def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 3200 != 0)

def day_of_week_jan1(year):
    return ( 1 + 5*((year - 1)%4) + 4*((year - 1)%100) + 6*((year-1)%400) ) % 7

def num_days_in_month(month_num, leap_year):
    return [31,29 if leap_year else 28,31,30,31,30,31,31,30,31,30,31][month_num-1]

def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    result=[["January","February","March","April","May","June","July","August","September","October","November","December"][month_num-1]]
    day_of_the_month = 1
    day_of_the_week = first_day_of_month
    week = "   " * first_day_of_month
    while day_of_the_month <= num_days_in_month:
        if day_of_the_week<=6:
            week += "{:>3}".format(day_of_the_month)
            day_of_the_month += 1
            day_of_the_week += 1
        else:
            result.append(week)
            week=""
            day_of_the_week = 0
    result.append(week)
    return result
        
def construct_cal_year(year):
    first,l = day_of_week_jan1(year),[year]
    for i in range(1,13):
        l.append(construct_cal_month(i,first,num_days_in_month(i,leap_year(year))))
        first = (first + num_days_in_month(i,leap_year(year)))%7
    return l
    
def display_calendar(year):
    # string = str(year) + '\n'
    string = ""
    for i in construct_cal_year(year)[1:]:
        string += i[0] + "\n" + "  S  M  T  W  T  F  S\n"
        for j in i[1:]:
            string += j + '\n'
        string += '\n'
    return string[:-2]