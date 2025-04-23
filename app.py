def fibonacci_generator(n):

    a=0
    b=1
    # Iterate n times to generate Fibonacci numbers
    for _ in range(n):
        yield a
        # Update a and b to the next Fibonacci numbers
        a, b = b, a + b

# Get user input
try:
    num = int(input("Enter how many Fibonacci numbers you want: "))
    if num < 0:
        print("Please enter a positive number.")
    else:
        print("Fibonacci sequence:")
        for val in fibonacci_generator(num):
            print(val, end=' ')
except ValueError:
    print("Invalid input. Please enter a valid integer.")