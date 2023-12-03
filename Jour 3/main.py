def lireFichierEtCalculer(cheminFichier):
    with open(cheminFichier) as file:
        lignes = [ligne.rstrip() for ligne in file.readlines()]

    sommeNombres = 0
    sommeRatios = 0

    nombreLignes = len(lignes)
    longueurLigne = len(lignes[0])

    compteurEngrenages = [[0] * longueurLigne for _ in range(nombreLignes)]
    produitEngrenages = [[1] * longueurLigne for _ in range(nombreLignes)]

    for indexLigne in range(nombreLignes):
        indexCaractere = 0
        while indexCaractere < longueurLigne:
            compteCaracteres = 1
            while indexCaractere < longueurLigne - 1 and lignes[indexLigne][indexCaractere].isdigit() == \
                    lignes[indexLigne][indexCaractere + 1].isdigit():
                compteCaracteres += 1
                indexCaractere += 1
            if lignes[indexLigne][indexCaractere].isdigit():
                nombre = int(lignes[indexLigne][indexCaractere - compteCaracteres + 1:indexCaractere + 1])
                estAdjacentSymbole = False
                for x in range(indexLigne - 1, indexLigne + 2):
                    for y in range(indexCaractere - compteCaracteres, indexCaractere + 2):
                        if 0 <= x < nombreLignes and 0 <= y < longueurLigne and lignes[x][y] != "." and not lignes[x][
                            y].isdigit():
                            estAdjacentSymbole = True
                        if 0 <= x < nombreLignes and 0 <= y < longueurLigne and lignes[x][y] == "*":
                            compteurEngrenages[x][y] += 1
                            produitEngrenages[x][y] *= nombre
                            break
                if estAdjacentSymbole:
                    sommeNombres += nombre
            indexCaractere += 1

    for indexLigne in range(nombreLignes):
        for indexCaractere in range(longueurLigne):
            if compteurEngrenages[indexLigne][indexCaractere] == 2:
                sommeRatios += produitEngrenages[indexLigne][indexCaractere]

    return sommeNombres, sommeRatios


# Lire le fichier et calculer les résultats
sommeNombres, sommeRatios = lireFichierEtCalculer("input.txt")

print("Somme des nombres adjacents aux symboles :", sommeNombres)
print("Somme des rapports d'engrenages :", sommeRatios)
