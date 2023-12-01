def trouverCalibrationValues(cheminFichier: str):
    # Initialisation
    total = 0
    # Ouvrir le fichier en lecture seule
    fichier = open(cheminFichier, "r")
    # utilisez readline() pour lire la première ligne
    line = fichier.readline()
    while line:
        premierChiffreTrouve = False
        premierChiffre = 0
        dernierChiffre = 0
        for caractere in line:
            if caractere.isnumeric():
                if not premierChiffreTrouve:
                    premierChiffre = caractere
                    dernierChiffre = caractere
                    premierChiffreTrouve = True
                else:
                    dernierChiffre = caractere
        calibrationValue = int(premierChiffre + dernierChiffre)
        total += calibrationValue

        line = fichier.readline()
    fichier.close()

    return total


def trouverCalibrationValuesV2(cheminFichier: str):
    # Initialisation
    total = 0
    # Ouvrir le fichier en lecture seule
    fichier = open(cheminFichier, "r")
    # utilisez readline() pour lire la première ligne
    line = fichier.readline()

    chiffresLettresAssoc = [["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
                            ['1', '2', '3', '4', '5', '6', '7', '8', '9']]

    while line:
        premierChiffreTrouve = False
        premierChiffre = '0'
        dernierChiffre = '0'
        caracteresLignes = ""
        for caractere in line:
            caracteresLignes += caractere

            chiffreLettreTrouves = []
            for element in chiffresLettresAssoc[0]:
                if element in caracteresLignes:
                    chiffreLettreTrouves.append(element)
                    break

            if chiffreLettreTrouves:
                index = chiffresLettresAssoc[0].index(chiffreLettreTrouves[0])
                chiffreLettre = chiffresLettresAssoc[1][index]
                if not premierChiffreTrouve:
                    premierChiffre = chiffreLettre
                    dernierChiffre = chiffreLettre
                    premierChiffreTrouve = True
                else:
                    dernierChiffre = chiffreLettre
                caracteresLignes = caracteresLignes[-1]
            elif caractere.isnumeric():
                if not premierChiffreTrouve:
                    premierChiffre = caractere
                    dernierChiffre = caractere
                    premierChiffreTrouve = True
                else:
                    dernierChiffre = caractere
                caracteresLignes = caracteresLignes[-1]

        calibrationValue = int(premierChiffre + dernierChiffre)
        total += calibrationValue

        line = fichier.readline()
    fichier.close()

    return total


calibrationValues = trouverCalibrationValues("input.txt")
calibrationValuesV2 = trouverCalibrationValuesV2("input.txt")
print(calibrationValues)
print(calibrationValuesV2)
