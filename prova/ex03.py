def globo_ou_sbt():
  print('---------- globo ou sbt ----------')
  print('[ a ] globo')
  print('[ b ] sbt')
  print('[ z ] SAIR')
  print('-----------------------------------')
  opcao = ''

  while opcao != 'z' and opcao != 'Z':
    opcao = input('Sua opção: ')
    if opcao != 'a' and opcao != 'b' and opcao != 'z' and opcao != 'Z':
      while opcao != 'a' and opcao != 'b' and opcao != 'z' and opcao != 'Z':
        print('Opção inválida. Tente novamente')
        opcao = input('Sua opção: ')
        if opcao == 'a' or opcao == 'b' or opcao == 'z' or opcao == 'Z':
          break
    if opcao == 'a':
      print('globo')
    elif opcao == 'b':
      print('sbt')
    elif opcao == 'z' or opcao == 'Z':
      break


globo_ou_sbt()