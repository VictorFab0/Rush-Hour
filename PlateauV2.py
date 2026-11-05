class plateau:
    """Classe créant un plateau 6x6"""

    def __init__(self):
        self.plateau = []

        nombre = 1

        for ligne in range(6):
            ligne_plateau = []

            for colonne in range(6):
                ligne_plateau.append([str(nombre)])
                nombre += 1

            self.plateau.append(ligne_plateau)

        print(self.plateau)
