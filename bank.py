saldo = 0

print("Välkommen till swedbank")
login = input("SKriv in ditt lösenord")

if login == "lösenord":
    print("välkommen till ditt konto")
    print("ditt saldo är: " +str(saldo) + "kr")
else:
    print("fel lösenord")

meny = input(" Vad vill du välja [i]insättning--[u]ttag-[a]vsluta: ")

if meny == "i":
    insätt = float(input("hur mycket vill du sätta in?: "))
    saldo += insätt
elif meny == "u":
    utdrag = float(input("Hur mycket vill du ta ut?:"))
elif meny == "a":
    print("ha en trevlig dag")

print(str(saldo) + "kr")

