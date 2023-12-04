import sys


def calculate_section_sum():
    start, end = map(int, sys.stdin.readline().split())
    number = 1
    total_sum = 0
    sequence = []

    while len(sequence) <= end:
        sequence.extend([number] * number)
        number += 1

    for i in sequence[start-1:end]:
        total_sum += i

    return total_sum


print(calculate_section_sum())
