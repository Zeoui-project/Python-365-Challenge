# %% [markdown]
# # Primes smaller than or equal to the Number

# %%
def SieveOfEratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while(p * p <= n):
        # if p is not marked as False, this it is a prime
        if(primes[p]) == True:
            # mark all multiples of number as False
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    # Printing all primes
    for i in range(2, n):
        if primes[i]:
            print(i)

if __name__ == '__main__':
    n = int(input("Enter a number to check all smaller prime numbers"))
    SieveOfEratosthenes(n)


