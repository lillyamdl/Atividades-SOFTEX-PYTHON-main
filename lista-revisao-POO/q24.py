#Crie uma função que atualiza a idade de uma pessoa em um dicionário.

def atualizar_idade(pessoa,nova_idade):
    pessoa['idade'] = nova_idade #
    return pessoa

pessoa = {
    'nome' : 'ana',
    'idade' : 25
}

nova_idade = 30
print(atualizar_idade(pessoa,nova_idade))