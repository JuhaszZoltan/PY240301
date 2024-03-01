from module import *

kategoriak:list[Kategoria] = []
file = open('titanic.txt', 'r', encoding='utf-8')
for sor in file:
    kat:Kategoria = Kategoria(sor)
    kategoriak.append(kat)

print(f'2. feladat: {len(kategoriak)} db')

utasok_szama:int = 0
for kat in kategoriak:
    utasok_szama += (kat.eltuntek_szama + kat.tulelok_szama)
print(f'3. feladat: {utasok_szama} fő')

van_talalat:bool = False
kulcsszo:str = input('4. feladat: kulcsszo: ')
for kat in kategoriak:
    if kulcsszo in kat.kategoria_nev:
        print('\tvan találat!')
        van_talalat = True
        break
else: print('\tnincs találat!')

if van_talalat:
    print('5. feladat:')
    for kat in kategoriak:
        if kulcsszo in kat.kategoria_nev:
            print(f'\t{kat.kategoria_nev} {kat.eltuntek_szama + kat.tulelok_szama} fő')

print('6. feladat:')
for kat in kategoriak:
    if (kat.eltuntek_szama + kat.tulelok_szama) * .6 < kat.eltuntek_szama:
        print(f'\t{kat.kategoria_nev}')

maxi:int = 0
for i in range(1, len(kategoriak)):
    if kategoriak[i].tulelok_szama > kategoriak[maxi].tulelok_szama:
        maxi = i
print(f'7. feladat: {kategoriak[maxi].kategoria_nev}')

for i in range(len(kategoriak) - 1):
    for j in range(i+1, len(kategoriak)):
        if kategoriak[i].eltuntek_szama < kategoriak[j].eltuntek_szama:
            csere:Kategoria = kategoriak[i]
            kategoriak[i] = kategoriak[j]
            kategoriak[j] = csere
for kat in kategoriak:
    print(f'{kat.kategoria_nev} eltuntek szama: {kat.eltuntek_szama}')