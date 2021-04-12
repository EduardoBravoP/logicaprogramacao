def criar_lista(n):
  lista = []

  for i in range(n):
    lista.append(input('Digite um valor para a lista: '))
  
  return lista


tamanho_da_lista = int(input('Digite o tamanho da lista: '))
criar_lista(tamanho_da_lista)