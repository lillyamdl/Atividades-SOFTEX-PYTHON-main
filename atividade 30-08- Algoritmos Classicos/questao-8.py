# Crie uma função recursiva que some os dígitos de um número (ex.: 123 → 1+2+3 = 6).

def soma(n):
    if n == 0:
        return 0
    else:
        return n % 10 + soma(n // 10)

print(soma(123))

# 123 % 10 = 3 +  12 % 10 = 2 + 1 % 10 = 1 = 6