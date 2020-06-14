# Problem 4
# 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# 
# Author: Jose Manuel Martinez Salas

digits_number = 2
n1 = 1
n2 = 1

while len(str(n1)) < (digits_number +1):
    n1 = n1 + 1

print(n1)