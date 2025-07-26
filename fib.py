# escreva uma função para gerar números de Fibonacci
# que recebe um inteiro n e retorna uma lista com os n primeiros números de Fibonacci.
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


def fib(terno):
    if terno == 0:
        return 0
    elif terno == 1:
        return 1
    return fib(terno - 1) + fib(terno - 2)
  
# escreva programa principal que solicita ao usuário um número inteiro n
# e exibe os n primeiros números de Fibonacci usando a função fibonacci.
n = int(input("Digite um número inteiro: "))
print(fibonacci(n))

# teste de fib:
print(fib(9))  # Exemplo de chamada da função fib para o décimo termo
