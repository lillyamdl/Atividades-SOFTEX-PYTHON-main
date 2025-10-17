num = int(input(f"Coloque um número: "))
print(f"Tabuada do numero {num}")

for i in range(1, 11):
    resultado = i * num
    print(f"{i} x {num} = {resultado}")