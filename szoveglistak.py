szoveg_lista=["Alma", "Körte", "Szilva", "Szölö", "alma", "Eszencia"]

"""
1. Hány Alma/alma van a listában?
"""
def elso():
    db:int=0
    for i in range (0,len(szoveg_lista), 1):
        if szoveg_lista[i].lower()== "alma":
            db+=1
    print(f"Az alma szó {db} van")
    return db


"""2. Hány Sz betűvel kezdödö szöveg van a listában"""
def masosik():
    db:int=0
    for i in range (0, len(szoveg_lista),1):
        if (szoveg_lista[i])[0:2].rfind("Sz") :
            db+=1
    print(f"Sz betűk darab száma:{db}")
    print()
    return db

"""3. Melyik a leghosszab szó? Mekkora a hossza? Hányadik helyen áll a lsitábam?"""
def harmadik():
    leghosszab:str=""
    max_hossz:int=0
    index:int=0
    for i in range (0, len(szoveg_lista),1):
        if  len(szoveg_lista[i]) > len(leghosszab) :
            leghosszab = szoveg_lista[i]
            index=i+1
    print(f"A leghossszab szó:{leghosszab}. Hossza:{len(leghosszab)}. A {index} helyen áll")
    return leghosszab