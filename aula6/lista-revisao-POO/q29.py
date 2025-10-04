#Compare duas tuplas representando dados (ano, mês, dia) e veja qual é mais recente

data1 = (2025,12,3)
data2 = (2024,4,7)

if data1 > data2:
    print(f"{data1} é mais recente que {data2}")
elif data2 > data1:
    print(f"{data2} é mais recente que {data1}")
else:
    print(f"sao iguais em periodo de tempo")

