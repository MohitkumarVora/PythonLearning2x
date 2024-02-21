# Using only for loop and if condition
limit = int(input("Enter the limit for Fibonacci sequence: "))
fib_sequence = [0, 1]  # Initialize Fibonacci sequence with first two numbers

if limit == 0:
    fib_sequence = [0]
elif limit == 1:
    fib_sequence = [0, 1]
else:
    for i in range(2, limit):
        next_fib = fib_sequence[-1] + fib_sequence[-2]  # fib_sequence initialize in line 2
        if next_fib > limit:
            break
        # fib_sequence.append(next_fib)  # Using list append function
        fib_sequence = fib_sequence + [next_fib]  # Using list concatenation instead of append

print("Fibonacci sequence up to", limit, ":", fib_sequence)

# Using Function


def fibonacci_series(number):
    fib_seq = [0, 1]
    for seq in range(2, number):
        new_number = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(new_number)
    print("Fibonacci series is:", fib_seq)


Number = int(input("Enter the level of fibonacci series: "))
fibonacci_series(Number)
