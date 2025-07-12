import datetime

start=datetime.date(2000,1,1)
end=datetime.date(2020,10,1)
days=datetime.timedelta(days=1)
total=0

while start<=end:
    if start.day==1 or start.weekday()==0:
        total+=2
    else:
        total+=1
    start+=days
print(total)