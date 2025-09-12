numero = int(input())
if numero <10:
    print('piqueno')
else:
    if 10 < numero and numero < 50:
        print('mediano')
        if numero > 50:
            print('grande') 