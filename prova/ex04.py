def tipo_de_professor(medias):
  medias_menores_que_7 = 0
  porcentagem = len(medias) * 0.25

  for media in medias:
    if media < 7:
      medias_menores_que_7 += 1
  if medias_menores_que_7 < porcentagem:
    return 'Professor coxa'
  else:
    return 'Professor padrão'


tipo_de_professor([5, 9, 10, 10, 5])
