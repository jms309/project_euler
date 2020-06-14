# Problem 3
# 
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# 
# Author: Jose Manuel Martinez Salas

N = 600851475143
p = 2
factors = []

while(N > p**2):
    if N % p == 0:
        factors.append(p)
        N = N/p
    else:
        p = p + 1
        
factors.append(N)
print(max(factors))