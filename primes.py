"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
"""Website used for Error handling documentation:
    https://docs.python.org/3/tutorial/errors.html
"""

def primes(number_of_primes):
    if number_of_primes<=0:
        raise ValueError(f'number was {number_of_primes}. It should be more than 0')

    list = []
    count=2


    while number_of_primes!=0:
        for i in range(2,count):
            if(count%i==0):
                break
        else:
            list.append(count)
            number_of_primes-=1
        count+=1

    return list

print(primes(10))
print(primes(-1))