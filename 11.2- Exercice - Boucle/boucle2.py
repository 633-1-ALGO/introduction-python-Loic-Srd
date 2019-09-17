# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]
print("Tableau :",B)
for i in range(0, len(B)):
    x = B[i]
    y = i
    while y > 0 and B[y-1] > x:
        B[y] = B[y-1]
        y = y-1
    B[y] = x
print("Tableau trier par insertion:",B)
