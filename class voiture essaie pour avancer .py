class Voiture:
  """Classe créeant une voiture sur le plateau"""
  def __init__(self, couleur, taille, symbole, coordonnees_x,coordonnees_y ):
    """initialisation d'une voiture dont la taille est comprise entre 2 et 3 compris. 
    La voiture rouge est réservée à la voiture à faire sortir."""
    
    self.taille = taille 
    if 0<=self.coordonnees_x<=5 :
      self.coordonees_x = coordonnees_x
    else : 
      print ("Les coordonnées doivent être compris entre 0 et 5 pour qu'elles puissent concorder avce le tableau !") 
    if 0<=self.coordonnees_y<=5 :
      self.coordonees_y = coordonnees_y
      print ("Les coordonnées doivent être compris entre 0 et 5 pour qu'elles puissent concorder avce le tableau !")
    if self.couleur = "rouge" : 
      self.couleur = couleur
      self.taille = 2
      self.symbole = "r"
      self.coordonnees_x = 2
      self.coordonnees_y = 0
    else : 
      self.couleur = couleur


  def avancer (self, nb_cases) :
    
    
 
"""
taille = 6
Plateau = []

for ligne in range(taille):
    Plateau.append(["x"] * taille)

voiture = Voiture_rouge(3, 3)
"""

for i in range(voiture.taille):
    Plateau[voiture.coordonnees_x][voiture.coordonnees_y + i] = "r"
for ligne in range(taille):
    affichage = ""
    for colonne in range(taille):
        affichage += Plateau[ligne][colonne] + " "
    print(affichage)
