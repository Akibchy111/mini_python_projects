#Python program to write weight into a file

from datetime import date
from sys import argv

weight = float(argv[1])

def get_str(weight):
    today_date = date.today()

    day_suffix = 'th'

    num_day = int(str(today_date).split('-')[2])

    if num_day in [1, 2, 3, 21, 22, 23]:
        if num_day % 10 == 1:
            day_suffix = 'st'
        elif num_day % 10 == 2:
            day_suffix = 'nd'
        else:
            day_suffix = 'rd'

    
    string = today_date.strftime("%B %d") + ('%s' % day_suffix) + today_date.strftime(', %Y') \
            + (' -- %.1f lbs' % weight)

    return string

def weight_input(weight):

    print('Weight entering: %.1f lbs' % weight)

    with open('/home/akibchy111/Documents/weightTracker' , 'a') as file:
        file.write('\n' + get_str(weight))

    print(get_str(weight))

   
weight_input(weight)

    
