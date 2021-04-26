lista = ["alo ", " Alo ", " aLO ", " alO"]

print(list(map(lambda x: x.replace(' ', '').lower(), lista)))
