import datetime
import calendar

ans = 0

for year in range(1901, 2001):
	for month in range(1,13):
		monthmax=calendar.monthrange(year,month)
		monthmax=monthmax[1]
		working=datetime.date(year,month,1)
		if working.month!=month:
			break

		if working.weekday() == 6:
			print ("Date" , working, ans)
			ans=ans+1

print ("Answer:"+str(ans))

