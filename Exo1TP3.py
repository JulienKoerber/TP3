#Exercice1 a TP3
N = int(input("Entrez la valeur de N : "))
somme = 0
for i in range(N + 1):
    somme += i
print("Somme de 0 à", N, "=", somme)




#Exercice1 b TP3
while True:
    valeur= int(input("Veuillez entrer une valeur"))
    if valeur== 100:
        print("La valeur est à 100. La boucle se termine")
        break
    else:
        print("La valeur n'est pas 100. Renvoyez une valeur.")


#Exercice1 c TP3
count_inf_10 = 0
count_10_to_15 = 0
count_sup_15 = 0

for _ in range(10):
    valeur = float(input("Saisissez une valeur entre 0 et 20: "))

    while valeur < 0 or valeur > 20:
        valeur = float(input("La valeur n'est pas comprise entre 0 et 20: "))
    if valeur < 10:
        count_inf_10 += 1
    elif valeur < 15:
        count_10_to_15 += 1
    else:
        count_sup_15 += 1
print(f"Nombre de valeurs inférieures strictement à 10 : {count_inf_10}")
print(f"Nombre de valeurs supérieures ou égales à 10 et inférieures strictement à 15 : {count_10_to_15}")
print(f"Nombre de valeurs supérieures ou égales à 15 : {count_sup_15}")


#Exercice1 d TP3
X = float(input("Veuillez saisir un nombre supérieur à 1 (X) : "))
N = 0
somme = 0
while somme <= X:
    somme += N
    N += 1
N -= 1
print("Le plus grand nombre N tel que la somme soit inférieure ou égale à", X, "est :", N)
