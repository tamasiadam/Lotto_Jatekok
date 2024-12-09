import random

print("Üdvözöllek a játékban!")

jatekos = []

generalt_szamok = {random.randint(1, 10) for i in range(5)}


while len(jatekos) < 5:
    jatekos_szamok = int(input("Adj meg egy számot! "))    
    if jatekos_szamok in jatekos:
        print("Te butus! Ez má' vót'")
    elif jatekos_szamok >= 1 and jatekos_szamok <= 90:
        jatekos.append(jatekos_szamok)
    else:   
        print("Ez nem jóÓ!!")

talalat = 0

for szam in talalat :
    if jatekos in generalt_szamok:
        talalat += 1

print(f"A te számaid: {jatekos}")
print(f"Nyerőszámok: {generalt_szamok}")
print(f"Találat: {talalat}")


#Problémák:
#nyerőszámok ne lehessen ugyanaz
#találat számláló