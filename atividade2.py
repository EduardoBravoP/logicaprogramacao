def calcula_soma(lista):
  soma_das_notas = 0

  for nota in lista:
    soma_das_notas += nota

  return soma_das_notas

def converte_entrada(texto):
  lista = texto.split(' ')

  lista = [float(string) for string in lista]
  return lista

def processa_numeros(lista):
  soma = calcula_soma(lista)
  numero_de_elementos = len(lista)

  return (soma, numero_de_elementos)


def main():
  entrada = input('Digite números separados por espaço ')
  
  lista_com_numeros = converte_entrada(entrada)
  media = processa_numeros(lista_com_numeros)
  
  media = media[0] / media[1]

  print(f'A média desses números é {media:.2f}')


if __name__ == '__main__':
  main()