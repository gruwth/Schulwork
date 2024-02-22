from datetime import datetime
import locale


locale.setlocale(locale.LC_TIME, 'de_DE')

now = datetime.now()

formatted_time = now.strftime("%A, %d.%m.%Y %H:%M")
calender_week = now.isocalendar()[1]

print(formatted_time, "\nKW:", calender_week)
input()