#Print the Fibonacci series up to n terms
n int(input("Enter the number of terms for Fibonacci series: "))
a, b = 0, 1
fib = []
for i in range(n):
    fib.append(a)
    a, b = b, a + b
print(f"Fibonacci series ({n} terms): {fib}")
