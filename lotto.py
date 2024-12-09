import random

print("Üdvözöllek a játékban! 👋")



def otos_lotto():

    print("Üdv az ötös lottóban!")
    jatekos = []

    generalt_szamok = {random.randint(1, 91) for i in range(5)}
    sorszam = 1

    while len(jatekos) < 5:
        jatekos_szamok = int(input(f"Kérlek add meg a(z) {sorszam}. számot! "))
        if jatekos_szamok in jatekos:
            print("Ez a szám már volt! ❌")
        elif jatekos_szamok >= 1 and jatekos_szamok <= 90:
            sorszam += 1
            jatekos.append(jatekos_szamok)
        else:   
            print("Helytelen szám! ❌")

    talalat = generalt_szamok.intersection(jatekos)

    print(f"A te számaid: {jatekos}")
    print(f"Nyerőszámok: {generalt_szamok}")
    print(f"{len(talalat)} darab találatod van.")
    if len(talalat) == 5:
        print("Gratulálok, megnyerted a játékot! 🏆")
    else:
        print("Sok szerencsét legközelebb! 🍀")

def hatos_lotto():

    print("Üdv a hatos lottóban!")
    jatekos = []

    generalt_szamok = {random.randint(1, 46) for i in range(6)}
    sorszam = 1

    while len(jatekos) < 6:
        jatekos_szamok = int(input(f"Kérlek add meg a(z) {sorszam}. számot! "))
        if jatekos_szamok in jatekos:
            print("Ez a szám már volt! ❌ \n")
        elif jatekos_szamok >= 1 and jatekos_szamok <= 45:
            sorszam += 1
            jatekos.append(jatekos_szamok)
        else:
            print("Helytelen szám! ❌ \n")

    talalat = generalt_szamok.intersection(jatekos)

    print(f"A te számaid: {jatekos}")
    print(f"Nyerőszámok: {generalt_szamok}")
    print(f"{len(talalat)} darab találatod van.")
    if len(talalat) == 6:
        print("Gratulálok, megnyerted a játékot! 🏆")
    else:
        print("Sok szerencsét legközelebb! 🍀")

def hetes_lotto():

    print("Üdv a hetes lottóban!")
    jatekos = []

    generalt_szamok = {random.randint(1, 46) for i in range(6)}
    sorszam = 1

    while len(jatekos) < 7:
        jatekos_szamok = int(input(f"Kérlek add meg a(z) {sorszam}. számot! "))
        if jatekos_szamok in jatekos:
            print("Ez a szám már volt! ❌ \n")
        elif jatekos_szamok >= 1 and jatekos_szamok <= 35:
            sorszam += 1
            jatekos.append(jatekos_szamok)
        else:   
            print("Helytelen szám! ❌ \n")

    talalat = generalt_szamok.intersection(jatekos)

    print(f"A te számaid: {jatekos}")
    print(f"Nyerőszámok: {generalt_szamok}")
    print(f"{len(talalat)} darab találatod van.")
    if len(talalat) == 7:
        print("Gratulálok, megnyerted a játékot! 🏆")
    else:
        print("Sok szerencsét legközelebb! 🍀")

def kezdes():

    while True:
        jatek_valasztas = int(input("Válassz játékot!\nÖtös lottó (1)\nHatos lottó (2)\nHetes lottó (3)\nVálassz!: "))
        if jatek_valasztas == 1:
            print("Ötös lottó kiválasztva! ✅")
            otos_lotto()
        if jatek_valasztas == 2:
            print("Hatos lottó kiválasztva! ✅")
            hatos_lotto()
        if jatek_valasztas == 3:
            print("Hetes lottó kiválasztva! ✅")
            hetes_lotto()
        else:
            print("Helytelen formátum! ❌")

kezdes()