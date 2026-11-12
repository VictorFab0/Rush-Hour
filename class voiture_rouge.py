
class Voiture_rouge:
    """Classe créant la voiture rouge (toujours horizontale)"""
    def __init__(self, coordonnees_x, coordonnees_y):
        if 0 <= coordonnees_x <= 5 and 0 <= coordonnees_y <= 4:
            self.coordonnees_x = coordonnees_x
            self.coordonnees_y = coordonnees_y
            self.couleur = "rouge"
            self.taille = 2
            self.symbole = "r"
            self.orientation = "H"
        else:
            print("Coordonnées pas bonnes")

    def avancer(self, nb_cases, plateau):
        """Déplace la voiture rouge"""
        # Effacer ancienne position
        for i in range(self.taille):
            plateau.grille[self.coordonnees_x][self.coordonnees_y + i] = "x"
        
        # Mettre à jour
        self.coordonnees_y += nb_cases
        
        # Nouvelle position
        for i in range(self.taille):
            plateau.grille[self.coordonnees_x][self.coordonnees_y + i] = self.symbole
