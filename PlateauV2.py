class Plateau:
    """Classe créant et gérant le plateau de jeu 6x6"""
    def __init__(self):
        self.taille = 6
        self.grille = []

        for ligne in range(self.taille):
            self.grille.append(["x"] * self.taille)

    def afficher(self):
        """Affiche le plateau dans la console"""
        print("  0 1 2 3 4 5")
        for i in range(self.taille):
            sortie = "  <-- SORTIE" if i == 2 else ""
            print(f"{i} " + " ".join(self.grille[i]) + sortie)
        print()
