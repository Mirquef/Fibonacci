def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Imprimir los primeros 10 números de la secuencia de Fibonacci
n = 10
print(f"Los primeros {n} números de la secuencia de Fibonacci son: {fibonacci(n)}")
