import random

print("Üdvözöllek a játékban! 👋")

jatekos = []

generalt_szamok = {random.randint(1, 91) for i in range(5)}
sorszam = 0

while len(jatekos) < 5:
    sorszam += 1
    jatekos_szamok = int(input(f"Kérlek add meg a {sorszam}. számot! "))
    if jatekos_szamok in jatekos:
        print("Ez a szám már volt! Válassz újat!")
    elif jatekos_szamok >= 1 and jatekos_szamok <= 90:
        jatekos.append(jatekos_szamok)
    else:   
        print("Helytelen szám! Válassz újat!")

talalat = generalt_szamok.intersection(jatekos)

print(f"A te számaid: {jatekos}")
print(f"Nyerőszámok: {generalt_szamok}")
print(f"{len(talalat)} darab találatod van.")
