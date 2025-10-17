def media_aluno(notas):
  return sum(notas) / len(notas)


alunos = {
    "baby" : (1,2,3),
    "zua" : (4,5,6),
    "cua" : (7,8,9)
}

for aluno, notas in alunos.items():
  media = media_aluno(notas)
  print(f"E a media de cada aluno {alunos} foi {media}")
print(f"As notas do aluno baby é {alunos['baby']}")

