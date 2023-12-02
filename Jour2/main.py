def retourJeu(cheminFichier: str, nbRouges, nbVerts, nbBleus):
    # Initialisation
    total = 0
    puissanceJeuTotal = 0
    # Ouvrir le fichier en lecture seule
    fichier = open(cheminFichier, "r")
    # utilisez readline() pour lire la première ligne
    line = fichier.readline()
    while line:
        idPartie = int(line.split(':')[0].split(' ')[1])

        informationsPartie = line.split(':')[1].split(';')
        maxVerts = 0
        maxRouges = 0
        maxBleus = 0
        for tirage in informationsPartie:
            for info in tirage.split(','):
                infoCouleur = info.strip().split(' ')
                match infoCouleur[1]:
                    case "green":
                        if int(infoCouleur[0]) > maxVerts:
                            maxVerts = int(infoCouleur[0])
                    case "red":
                        if int(infoCouleur[0]) > maxRouges:
                            maxRouges = int(infoCouleur[0])
                    case "blue":
                        if int(infoCouleur[0]) > maxBleus:
                            maxBleus = int(infoCouleur[0])
        puissanceJeuTotal += maxBleus * maxRouges * maxVerts
        if maxBleus <= nbBleus and maxRouges <= nbRouges and maxVerts <= nbVerts:
            total += idPartie
        line = fichier.readline()
    fichier.close()

    return [total, puissanceJeuTotal]


retour = retourJeu("input.txt", 12, 13, 14)
print(retour[0])
print(retour[1])
