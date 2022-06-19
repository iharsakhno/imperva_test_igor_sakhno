from datetime import datetime, timedelta

line_1 = str(input('Date(dd.mm.yyyy): '))
my_date = datetime.strptime(line_1, "%d.%m.%Y")
delta = int(input('number_of_days: '))

new_date = my_date + timedelta(days = delta)

print(new_date)
print(my_date)

