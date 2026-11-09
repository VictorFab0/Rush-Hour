class Voiture_rouge:
    """Classe créant la voiture rouge"""
    def __init__(self, coordonnees_x, coordonnees_y):
        if 0 <= coordonnees_x <= 5 and 0 <= coordonnees_y <= 4:
            self.coordonnees_x = coordonnees_x
            self.coordonnees_y = coordonnees_y
            self.couleur = "rouge"
            self.taille = 2
            self.symbole = "r"
        else:
            print("Coordonnées pas bonne")

taille = 6
Plateau = []

for ligne in range(taille):
    Plateau.append(["x"] * taille)

voiture = Voiture_rouge(2, 3)
for i in range(voiture.taille):
    Plateau[voiture.coordonnees_x][voiture.coordonnees_y + i] = "r"
for ligne in range(taille):
    affichage = ""
    for colonne in range(taille):
        affichage += Plateau[ligne][colonne] + " "
    print(affichage)
