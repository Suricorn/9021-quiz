# Written by *** for COMP9021
#
# Call "trinumber" any integer that is the product of
# 3 prime numbers, for instance:
# - 8, equal to 2 x 2 x 2
# - 363, equal to 3 x 11 x 11
# - 455, equal to 5 x 7 x 13
# - 231, equal to 3 x 7 x 11
# - 782, equal to 2 x 17 x 23
#
# Given a trinumber n, call "gap in its decomposition"
# the minimum of
# - the difference between second and first primes
#   in n's decomposition, and
# - the difference between third and second primes
#   in n's decomposition
# (ordering the 3 primes from smallest to largest).
# For instance,
# - the gap in the decomposition of 8 is 0 (2 - 2)
# - the gap in the decomposition of 363 is 0 (11 - 11)
# - the gap in the decomposition of 455 is 2 (7 - 5)
# - the gap in the decomposition of 231 is 4 (7 - 3 or 11 - 7)
# - the gap in the decomposition of 782 is 6 (23 - 17)
#
# Implements a function tri_numbers(n) that outputs:
# - the number of trinumbers at most equal to n included;
# - the largest trinumber at most equal to n included;
# - the maximum gap in the decomposition of trinumbers
#   at most equal to n included;
# - ordered from smallest to largest, the numbers having
#   that maximum gap in their decompositions,
#   together with their decompositions.
#
# You can assume that n is an integer at least equal to 8.
# In the tests, its value won't exceed 50_000_000.

from math import sqrt


def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve

def tri_numbers(n):
    dict = get_trinumbers(n)
    if (len(dict)==1):
        print("There is 1 trinumber at most equal to "+str(n)+".")
    else:
        print("There are",len(dict),"trinumbers at most equal to "+str(n)+".")
    largest = max(dict.keys())
    print("The largest one is " + str(largest) + ", equal to",dict[largest][1],"x",dict[largest][2],"x " + str(dict[largest][3])+".")
    print("")
    print("The maximum gap in decompositions is " + str(max([i[0] for i in dict.values()])) + ".")
    print("It is achieved with:")
    keys = dict.keys()
    for key in dict.keys():
        if (dict[key][0] == max([i[0] for i in dict.values()])):
            print(" ",key,"=",dict[key][1],"x",dict[key][2],"x",dict[key][3])

def get_primes(n):
    n=int(n/4)
    result = []
    sieve = sieve_of_primes_up_to(n)
    for i in range(2,n+1,1):
        if(sieve[i]):
            result.append(i)
    return result

def get_trinumbers(n):
    dict = {}
    primes = get_primes(n)
    for i in primes:
        for j in primes:
            for k in primes:
                trinumber = i*j*k
                if (trinumber <= n and trinumber not in dict):                  
                    dict[i*j*k] = (get_gap(i,j,k),i,j,k)
                
    return dict

def get_gap(i,j,k):
    return min(abs(j-i), abs(k-j))

tri_numbers(34)
