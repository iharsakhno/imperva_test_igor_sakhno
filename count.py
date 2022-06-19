date = input("Date ")
num = input("number_of_days: ")
count_month = 0
f_data = date.split(".")
f_data = [int(x) for x in f_data]
month_31 = [1, 3, 5, 7, 8, 12]
month_30 = [4, 6, 9, 10, 11]

print(f_data)

day = f_data[0]
month = f_data[1]
year = f_data[2]

def feb(month):
  if month == 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
      return 29
    else:
      return 28

print(feb(month))

def counts(month):
  if month in month_31:
    if num + day > 31:
      if num + day // 31 > 31:
        return count_month = month+1, count_day = (31 - day) + num
  if month in month_30:
    pass
  if month == 2:
    feb(month)









