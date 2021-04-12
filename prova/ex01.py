def calcula_media(nota1, nota2, nota3):
  media = (nota1 + nota2 + nota3) / 3

  return f'Média do aluno é {media:.2f}'


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

calcula_media(nota1, nota2, nota3)