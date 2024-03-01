from module import *

kategoriak:list[Kategoria] = []

file = open('titanic.txt', 'r', encoding='utf-8')
for sor in file:
    kat:Kategoria = Kategoria(sor)
    kategoriak.append(kat)

print(f'2. feladat: {len(kategoriak)} db')

utasok_szama:int = 0
for kat in kategoriak:
    utasok_szama += (kat.tulelok + kat.eltuntek)
print(f'3. feladat: {utasok_szama} fő')

kulcsszo:str = input('4. feladat: kulcsszó: ')
# i:int = 0
# while i < len(kategoriak) and kulcsszo not in kategoriak[i].nev:
#     i += 1
# if i < len(kategoriak):
#     print('\tvan találat!')
# else:
#     print('\tnincs találat!')

for kat in kategoriak:
    if kulcsszo in kat.nev:
        print('\tvan találat!')
        break
else: print('\tnincs találat!')


#a python buzis :3