from datetime import datetime

line_1 = str(input('Date(dd.mm.yyyy): '))
delta = int(input('number_of_days: '))
my_date = datetime.strptime(line_1, "%d.%m.%Y")
from datetime import timedelta
new_date = my_date + timedelta(days = delta)

print(my_date)
print(new_date)

