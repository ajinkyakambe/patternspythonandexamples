# 3. Python Program to Display Fibonacci Sequence Using Recursion

def fibonacci(N):
    if N == 0:
        return 0

    elif N == 1:
        return 1

    return fibonacci(N - 1) + fibonacci(N - 2)


# Driving code
inputnumber = 22

if inputnumber <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    fibonachiseq = []
    for i in range(inputnumber):
        fibonachiseq.append(fibonacci(i))
    print(fibonachiseq)
