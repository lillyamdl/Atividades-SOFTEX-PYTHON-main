#verificador de senha forteee

senha = input()

if any(c.islower() for c in senha)and any(c.isupper() for c in senha) and any(c.isdigit() for c in senha):
    if len(senha) >= 8:
        print("Senha forte")
    else:
        print("Senha fraca")
else:
    print("Senha fraca")