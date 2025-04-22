MAX_VALUE = 10000  # Constant for maximum value

def print_fibonacci_sequence():
    """Prints Fibonacci sequence terms up to MAX_VALUE."""
    # Initialize first two Fibonacci numbers
    a, b = 0, 1
    
    # Print the first term (Fib(0))
    print(a, end=' ')
    
    # Generate and print subsequent terms while they're < MAX_VALUE
    while b < MAX_VALUE:
        print(b, end=' ')
        a, b = b, a + b  # Update Fibonacci numbers

if __name__ == '__main__':
    print_fibonacci_sequence()