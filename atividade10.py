def imprima_ate(n):
  for i in range(n):
    if i % 5 == 0 and i % 2 == 1:
      print(i)

def cria_lista(n):
  lista = []

  for i in range(n):
    valor = input('Entre com um valor: ')
    lista.append(valor)
  return lista

def numeros_maiores_que_5(lista):
  maiores_que_5 = 0
  
  for i in lista:
    if i > 5:
      maiores_que_5 += 1
  return maiores_que_5

def psg_ou_bayern():
  print('---------- BAYERN OU PSG ----------')
  print('[ a ] PSG')
  print('[ b ] BAYERN')
  print('[ d ] SAIR')
  print('-----------------------------------')
  opcao = ''

  while opcao != 'd':
    opcao = input('Sua opção: ')
    if opcao != 'a' and opcao != 'b' and opcao != 'd':
      while opcao != 'a' and opcao != 'b' and opcao != 'd':
        print('Opção inválida. Tente novamente')
        opcao = input('Sua opção: ')
        if opcao == 'a' or opcao == 'b' or opcao == 'd':
          break
    if opcao == 'a':
      print('PSG')
    elif opcao == 'b':
      print('BAYERN')
    elif opcao == 'd':
      break


imprima_ate(100)
cria_lista(2)
numeros_maiores_que_5([0, 0, 1, 9, 10])
psg_ou_bayern()
