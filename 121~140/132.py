import sys
n = int(sys.stdin.readline())


def func(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * func(n - 1)


def func2():
    a = str(func(n))[::-1]
    b = 0
    for i in a:
        if i == '0':
            b += 1
        else:
            return b


print(func2())

n = int(sys.stdin.readline())


def count_trailing_zeros(n):
    count = 0
    i = 5
    while n / i >= 1:
        count += n // i
        i *= 5
    return count


print(count_trailing_zeros(n))

# 이 문제를 이해하는 핵심은 팩토리얼 계산 결과에 10이 곱해지는 경우, 즉 끝자리에 0이 추가되는 경우를 파악하는 것입니다. 10은 2와 5의 곱으로 이루어져 있습니다.
# 팩토리얼 계산에서는 각 숫자를 모두 곱하게 됩니다. 따라서 2와 5가 하나씩 있을 때마다 결과에 10이 곱해져서 끝자리에 0이 추가됩니다.
# 그런데 팩토리얼 계산에서는 대부분의 숫자가 2의 배수입니다. 예를 들어, 10!은 10, 8, 6, 4, 2와 같은 2의 배수를 여러 번 포함하게 됩니다. 따라서 2의 개수는 충분히 많습니다.
# 반면에 5의 배수는 10, 5와 같이 훨씬 적습니다. 따라서 2와 5의 쌍을 만드는 것은 결국 5의 개수에 의해 제한됩니다. 그래서 우리는 5의 배수의 개수만 세면 그것이 곧 끝자리 0의 개수가 됩니다. 이러한 이유로 2와 5의 쌍의 개수를 세는 것이 아니라 5의 개수만 세도 충분한 것입니다.
