#Prvočísla
#Vytvořil Matěj Matějka
import math


#Otevře soubor pro čtení
vstup = open("01.in", "r")
#Otevře soubor pro zápis
vystup = open("01.out", "w")
n = int(vstup.readline())
i = 0
while not i == n:
    delitel = 2
    num = int(vstup.readline())
    num = math.ceil(math.sqrt(num))
    i = i + 1
    while not delitel == num:
        #Pokud input je jedna
        if num == 1:
            vystup.write('\n' "SLOZENE")
            break
        #Dělení zadaného čísla
        if num % delitel == 0:
            vystup.write('\n' "SLOZENE")
            break
        delitel = delitel + 1
        #Pokud číslo není dělitelné bezezbytku
    if delitel == num:
        vystup.write('\n' "PRVOCISLO")
vstup.close()
vystup.close()
exit()