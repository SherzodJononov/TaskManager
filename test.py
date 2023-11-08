from datetime import datetime,time,date

# title = input("Enter a title :")
# description = input("Enter a description :")
# priority = input("Enter a priority :")
# due_date = input("Enter a date :")
# status = input("Enter a status :") 
from operator import itemgetter, attrgetter
nlist = []
name = {}
        
name['due_date'] = '01-09-2023'   
format_date = "%d-%m-%Y"   

day = datetime.strptime(name['due_date'],format_date)

print(day)