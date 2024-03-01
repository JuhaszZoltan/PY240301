from module import *

kategoriak:list[Kategoria] = []
file = open('titanic.txt', 'r', encoding='utf-8')
for sor in file:
    kat:Kategoria = Kategoria(sor)
    kategoriak.append(kat)

print(f'2. feladat: {len(kategoriak)} db')

utasok_szama:int = 0
for k in kategoriak:
    utasok_szama += (k.eltuntek + k.tulelok)
print(f'3. feladat: {utasok_szama} fő')

kulcsszok:str = input('4. feladat: kulcsszó: ')
for k in kategoriak:
    if kulcsszok in k.nev:
        print('\tvan találat!')
        break
else: print('\tnincs találat!')

meghaladta:list[Kategoria] = []

for kat in kategoriak:
    if (kat.eltuntek + kat.tulelok) * .6 < kat.eltuntek:
        meghaladta.append(kat)
print('6. feladat:')
for kat in meghaladta:
    print(f'\t{kat.}')