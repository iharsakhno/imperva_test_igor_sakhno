import datetime
import timestamp as timestamp

line_1 = str(input('Date(dd.mm.yyyy): '))
my_date = datetime.datetime.strptime(line_1, "%d.%m.%Y")
epoch_time = (timestamp(my_date)/1000)
delta = int(input('number_of_days: '))
one_day = 86400
range = one_day * delta
finish_date_epoch = range + epoch_time
mytimestamp = datetime.datetime.fromtimestamp(finish_date_epoch)
datetime_str = mytimestamp.strftime("%Y-%m-%d")

print("Your date is: " + datetime_str)

