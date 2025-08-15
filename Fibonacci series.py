#Find the sum of digits of a given number
num=int(input("Enter a number to find sum of its sum"))
n = num 
sum_digits = 0

while n > 0:
    sum_digits += n % 10
    n //= 10

print(f"Sum of digits of {num} is {sum_digits}")
