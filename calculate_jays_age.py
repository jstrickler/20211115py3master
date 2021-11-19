from datetime import date

today = date.today()

print(today)
print(today.month, today.year)

jays_bd = date(2014, 8, 1)

delta = today - jays_bd

years, days = divmod(delta.days, 365)

print(f"Jay is {years} years and {days} days old")

