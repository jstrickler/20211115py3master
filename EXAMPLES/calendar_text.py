#!/usr/bin/env python
import calendar

tcal = calendar.TextCalendar()  # <1>
print(tcal.formatmonth(2012, 1))  # <2>

print()
print(tcal.formatyear(2022))
