date = input("Date ")
num = input("number_of_days: ")
f_data = date.split(".")
f_data = [int(x) for x in f_data]
month_31 = [1, 3, 5, 7, 8, 12]
month_30 = [4, 6, 9, 10, 11]
month_29 = 29
month_28 = 28

print(f_data)

day = f_data[0]
month = f_data[1]
year = f_data[2]
if month == 2:
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(month_29)
    # return month_29
  else:
    pass
    # return month_28







