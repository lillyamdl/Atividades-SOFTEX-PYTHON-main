notas = {
    ('ana','matematica') : 4,
    ('ana', 'portugues') : 6,
    ('ana' , 'bio') : 10,
    ('biba' , 'matematica') : 6,
    ('biba' , 'portugues') : 7,
    ('biba' , 'bio') : 8
}

nome_aluno = input('me diga o nome de um aluno: ')

aluno_encontrado = False
soma = 0
disciplinas_notas = []
num_disciplinas = 0

for(aluno, disciplina), nota in notas.items():
    if aluno == nome_aluno:
        aluno_encontrado = True
        disciplinas_notas.append((disciplina, nota))
        soma += nota 
        num_disciplinas += 1

if aluno_encontrado:
    print(f"notas de {nome_aluno}")
    for disciplina, nota in disciplinas_notas:
        print(f"{disciplina} : {nota}")

        if num_disciplinas >0:
            media_geral = soma / num_disciplinas
        
        else:
            print(f"nao possui notas registradas")
else:
    print(f"aluno não encontrado")
print(f"média geral de {nome_aluno} : {media_geral:.2f}")