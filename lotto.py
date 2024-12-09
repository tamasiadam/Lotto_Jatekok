import random

print("Üdvözöllek a játékban!")

jatekos = []

generalt_szamok = {random.randint(1, 10) for i in range(5)}


while len(jatekos) < 5:
    jatekos_szamok = int(input("Adj meg egy számot! "))
    if jatekos_szamok in jatekos:
        print("Ez a szám már volt! Válassz újat!")
    elif jatekos_szamok >= 1 and jatekos_szamok <= 90:
        jatekos.append(jatekos_szamok)
    else:   
        print("Helytelen szám! Válassz újat!")

# talalat = 0
# for szam in jatekos :
#      if jatekos_szamok in generalt_szamok:
#         talalat += 1

talalat = generalt_szamok.intersection(jatekos)
print(f"Találatok: {len(talalat)}")

print(f"A te számaid: {jatekos}")
print(f"Nyerőszámok: {generalt_szamok}")
print(f"Találat: {talalat}")


#Problémák:
#nyerőszámok ne lehessen ugyanaz
#találat számláló