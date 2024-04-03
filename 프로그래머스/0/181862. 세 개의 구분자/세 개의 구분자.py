def solution(myStr):
    list1 = ['a','b','c']
    for i in list1 :
        myStr = myStr.replace(i,' ')
    
    a = list(filter(lambda x: len(x) != 0, myStr.split(' '))) 
    return a if a else ['EMPTY']