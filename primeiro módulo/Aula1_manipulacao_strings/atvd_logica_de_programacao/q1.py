nome = input(f"Qual seu nome?")
idade = int(input(f"Qual sua idade?"))

if idade < 16:
    print(f"Você não pode votar")
else:
    print(f"Você pode votar")
