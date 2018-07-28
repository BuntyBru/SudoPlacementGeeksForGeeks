# Python 3 program to find a prime number
# pair whose sum is equal to given number
# Python 3 program to print super primes
# less than or equal to n.
 
# Generate all prime numbers less than n.
def SieveOfEratosthenes1(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
     
    arr=[]
    for p in range(2, n):
        if prime[p]:
            arr.append(p)
    return arr







def SieveOfEratosthenes(n, isPrime):
 
    # Initialize all entries of boolean
    # array as True. A value in isPrime[i]
    # will finally be False if i is Not a
    # prime, else True bool isPrime[n+1]
    isPrime[0] = isPrime[1] = False
    for i in range(2, n+1):
        isPrime[i] = True
 
    p = 2
    while(p*p <= n):
     
        # If isPrime[p] is not changed,
        # then it is a prime
        if (isPrime[p] == True):
         
            # Update all multiples of p
            i = p*2
            while(i <= n):
                isPrime[i] = False
                i += p
        p += 1
         
# Prints a prime pair with given sum
def findPrimePair(n):
 
    # Generating primes using Sieve
    isPrime = [0] * (n+1)
    SieveOfEratosthenes(n, isPrime)
 
    # Traversing all numbers to find 
    # first pair
    for i in range(0, n):
     
        if (isPrime[i] and isPrime[n - i]):
            
            return True

        
             
# Driven program
n =1
for i in range(n):
    n1 = 20
    prime_arr = SieveOfEratosthenes1(n1+1)
    print(prime_arr)
    count =0
    for i in range(len(prime_arr)):
        if findPrimePair(prime_arr[i]):
            count =count+1
    print(count)