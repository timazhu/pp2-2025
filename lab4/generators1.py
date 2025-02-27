#Create a generator that generates the squares of numbers up to some number N.

def squares(N):
    for i in range(1, N+1):
        yield i ** 2

N = int(input())
for n in squares(N):
    print(n)
    
#N=5
#1
#4
#9
#16
#25