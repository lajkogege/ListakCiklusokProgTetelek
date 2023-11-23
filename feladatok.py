import math
"""
1.Írj metodust, ami a paraméterben kapott lista elemeit kiírja a képernyőre
"""
import math


def elso(szam_lista):
    for i in range(0, len(szam_lista), 1):
        print(f"Az {i}. szám: {szam_lista[i]}")
        i+=1
    print()


"""
2.Mennyi a pozitív számok összege? -Összegzés
"""
def masodik(szam_lista):
    osszegzes:float=0
    for i in range (0,len(szam_lista),1):
        if szam_lista[i] >0:
            osszegzes += szam_lista[i]
        i+=0
    print(f"Pozítiv számok összege: {osszegzes}")
    print()
    return osszegzes



"""
3. Hány negatív szám van? -Megszámolás
"""
def harmadik(szam_lista):
    db:int=0
    for i in range(0,len(szam_lista),1):
        if szam_lista[i]<0:
            db+= 1
        i+=1
    print(f"A listában {db} negatív szám van.")
    print()
    return db


"""
4.Hány nem egész szám van a számok között? -Megszámolás 
"""
def negyedik(szam_lista):
    db:int=0
    for i in range (0, len(szam_lista), 1):
        if szam_lista[i] != math.floor(szam_lista[i]):
            db+=1
        i+=1
    print(f"A listban {db} nem egész szám van.")
    print()
    return db



"""
5. Mennyi a 3-mal osztható számok átlaga? -Összegzés -megszámolás
"""
def otodik(szam_lista):
    db:int=0
    osszegzes:int=0
    atlag:int=0
    for i in range(0,len(szam_lista),1):
        if szam_lista[i]%3==0:
            osszegzes+=szam_lista[i]
            db+=1
        i+=0
    osszegzes= math.floor(osszegzes/db)
    print(f"A listában 3-mal oszhtaó számok átlaga:{osszegzes} ")
    print()
    return osszegzes


"""
6. Mekkora a legnagyobb szám? -Max
"""
def hatodik(szam_lista):
    max:int=0
    legkisebb:int=0
    for i in range(0, len(szam_lista),1):
        if szam_lista[i]>legkisebb:
            max = szam_lista[i]
        i+=1
    print(f"Legnagyobb szám: {max}")
    print()
    return max

"""
7. Mekkora a legkisebb szám? -Min
"""
def hetedik(szam_lista):
    min:float=800
    for i in range (0, len(szam_lista),1):
        if szam_lista[i] <min:
            min=szam_lista[i]
        i+=1
    print(f"Legkisebb szám:{min}")
    print()
    return min

"""
8. Mekkora legkisebb és a legnagyobb szám különbsége? -Max
"""
def nyolcadik(szam_lista):

    max:float=hatodik(szam_lista)

    min: float = hetedik(szam_lista)
    print(f"Legkisebb szám:{min}")

    kulonbseg:float=max -min
    print(f"A két szám különbsége: +{kulonbseg}")
    print()
    return kulonbseg





