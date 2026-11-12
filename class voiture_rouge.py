# On importe les classes du fichier voiture.py
from voiture import Voiture, Voiture_rouge

class Plateau:
    """Plateau 6x6 basé sur Plateau_filip_V2 avec gestion des coordonnées"""
    def __init__(self):
        # Grille 6x6 remplie de "." pour les cases vides
        self.grille = [["." for _ in range(6)] for _ in range(6)]

    def placer_voiture(self, voiture):
        """Vérifie les coordonnées et place la voiture sur la grille"""
        cases_a_occuper = []

        for i in range(voiture.taille):
            if voiture.orientation == "H":
                cx, cy = voiture.x, voiture.y + i
            else:  
                cx, cy = voiture.x + i, voiture.y

            # Vérification des limites du plateau (0 à 5)
            if not (0 <= cx <= 5 and 0 <= cy <= 5):
                print(f"Erreur : La voiture {voiture.couleur} sort du plateau en ({cx}, {cy}) !")
                return False

            # Vérification des collisions
            if self.grille[cx][cy] != ".":
                print(f"Erreur : Collision en ({cx}, {cy}) pour la voiture {voiture.couleur} !")
                return False

            cases_a_occuper.append((cx, cy))

        # Inscription du symbole sur la grille
        for cx, cy in cases_a_occuper:
            self.grille[cx][cy] = voiture.symbole
        return True

    def afficher(self):
        """Affiche proprement le plateau avec la sortie"""
        print("  0 1 2 3 4 5")
        for i in range(6):
            sortie = "  <-- SORTIE" if i == 2 else ""
            print(f"{i} " + " ".join(self.grille[i]) + sortie)
        print()
