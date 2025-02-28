#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def divisible_by_12(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
print(", ".join(map(str, divisible_by_12(n))))
#n=34
#0, 12, 24