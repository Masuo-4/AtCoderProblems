import datetime

now = datetime.datetime(2022, 8, 27, hour=21)
td_m = datetime.timedelta(minutes=int(input()))
ans = now + td_m

print(ans.strftime('%H:%M'))
