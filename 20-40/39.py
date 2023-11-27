import datetime


def func():
    nowDate = datetime.datetime.now()
    returnType = nowDate.strftime('%Y-%m-%d')
    return returnType


print(func())
