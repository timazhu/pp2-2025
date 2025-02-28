#Implement a generator that returns all numbers from (n) down to 0.

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for i in countdown(n):
    print(i)

#n=5
#5
#4
#3
#2
#1
#0