# Written by *** for COMP9021
#
# Watch https://www.youtube.com/watch?v=7DHE8RnsCQ8
#
# Implements a function centrifuge(n, k) that takes
# as first argument an integer n at least equal to 2,
# as second argument an integer k between 0 and n included,
# and returns True or False depending on whether it is
# possible to balance k identical test tubes
# in an n-hole centrifuge, respectively.

import math
from math import sqrt
import numpy as np


def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve

# POSSIBLY DEFINE OTHER FUNCTIONS
def prime_factors(num):
    prime_factor_list_n = []
    while num % 2 == 0:
        #print(2, )
        prime_factor_list_n.append(2)
        num = num / 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            #print(i, )
            prime_factor_list_n.append(i, )
            num = num / i

    if num > 2:
        #print(int(num))
        prime_factor_list_n.append(int(num))

#Delete repeated prime factors in the list
    prime_factor_list_n = list(dict.fromkeys(prime_factor_list_n))
    #print(prime_factor_list_n)
#Reverse the list to check the prime factors from the largest to the smallest
    #print(reverse_prime_list_n)
    return prime_factor_list_n



true_list = []
def is_sum_of_numbers(n, k, prime_factors):
    #dynamic programming
    true_list = prime_factors + [0]    
    #Check if each number from 0 to k can be added to true_list
    for x in range(n+1):
        for j in prime_factors:
            if x - j in true_list and x not in true_list:
                true_list.append(x)
                #return True
    return k in true_list

def centrifuge(n, k):
    answer = []
    prime_factor_list_n = prime_factors(n)
    if is_sum_of_numbers(n, k, prime_factor_list_n) == True and is_sum_of_numbers(n, n - k, prime_factor_list_n) == True:
        return True
    else:
        return False



