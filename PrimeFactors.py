#Problem statement : Create a function that returns a list containing the prime factors of whatever integer is passed to it.
#Probelm Link : https://edabit.com/challenge/8vBvgJMc2uQJpD6d7

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

list = primes(8912234)
print(list)
