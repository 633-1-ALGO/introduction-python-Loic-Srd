# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

# texte.split(' ')
# print(texte.split(' '))

print("Nombre d'occurence du mot exemple :", texte.count('exemple'))

texte = texte.replace('est', 'exemple')
print(texte)
print(texte[::-1])
