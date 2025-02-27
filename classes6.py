#Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.

class prime:
    def __init__(self, numbers):
        self.numbers = numbers

    def prime(self, n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def filter_primes(self):
        return list(filter(lambda x: self.prime(x), self.numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14]
prime_filter = prime(numbers)

prime_numbers = prime_filter.filter_primes()
print(prime_numbers) #[2, 3, 5, 7, 11, 13]
