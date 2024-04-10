from collections import Counter


def func(array):
    new_li = Counter(array)
    max_num = max(new_li.values())
    common_li = []

    for i, j in new_li.items():
        if j == max_num:
            common_li.append(i)

    if len(common_li) > 1:
        return -1

    return common_li[0]


func([1, 2, 3, 3, 3, 4])


# from collections import Counter
# Counter 는 인덱스와, 빈도를 dict 형태로 반환해준다.
# ex) Counter([1, 2, 3, 3, 3, 4]) // Counter({3: 3, 1: 1, 2: 1, 4: 1})
# Counter.items() 를 사용하면 key, value 값을 반환해준다.
# Counter.values() 를 사용하면 value 값을 반환해준다.
# Counter.keys() 를 사용하면 key 값을 반환해준다.
