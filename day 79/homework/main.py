def nak_years(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("yes")
    else:
        print("no")

nak_years(2020)