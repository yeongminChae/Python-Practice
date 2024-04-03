import datetime

def solution(date1, date2):
    dt1 = datetime.datetime(date1[0], date1[1], date1[2])
    dt2 = datetime.datetime(date2[0], date2[1], date2[2])
    td = str(dt1 - dt2).split(' ')
    return 1 if len(td) != 1 and int(td[0]) < 0  else 0