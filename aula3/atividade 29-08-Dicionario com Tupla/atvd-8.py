pontos_turisticos = {
    (1234,5678) : 'sao paulo',
    (4321,8907) : 'rio de janeiro'
}

coordenada_input = input("Digite as coordenadas no formato x,y: ")
try:
  x, y = map(int, coordenada_input.split(',')) 
  coordenadas = (x, y)

  if coordenadas in pontos_turisticos:
      print(f"O ponto turístico nessas coordenadas é: {pontos_turisticos[coordenadas]}")
  else:
      print("Nenhum ponto turístico encontrado para essas coordenadas.")
except ValueError:
  print("Formato de coordenada inválido. Por favor, use o formato x,y.")
