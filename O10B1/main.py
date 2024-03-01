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
i:int = 0 
while i < len(kategoriak) and kulcsszo not in kategoriak[i].nev:
    i += 1
if i < len(kategoriak):
    print('\tvan találat!')
    print('5. feladat:')
    for kat in kategoriak:
        if kulcsszo in kat.nev:
            print(f'\t{kat.nev} {kat.tulelok + kat.eltuntek} fő')
else:
    print('\tnincs találat!')

meghaladta:list[str] = []
for kat in kategoriak:
    if (kat.eltuntek + kat.tulelok) * 0.6 < kat.eltuntek:
        meghaladta.append(kat.nev)
print('6. feladat:')
for nev in meghaladta:
    print(f'\t{nev}')

maxi:int = 0
for i in range(1, len(kategoriak)):
    if kategoriak[i].tulelok > kategoriak[maxi].tulelok:
        maxi = i
print(f'7. feladat: {kategoriak[maxi].nev}')