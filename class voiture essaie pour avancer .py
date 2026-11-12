class Voiture:
  """Classe créeant une voiture sur le plateau"""
  def __init__(self, couleur, taille, symbole, coordonnees_x,coordonnees_y ):
    """initialisation d'une voiture dont la taille est comprise entre 2 et 3 compris. 
    La voiture rouge est réservée à la voiture à faire sortir."""
    self.symbole = couleur[0].upper()
    if 1<self.taille<3 : 
      self.taille= taille 
    else : 
      print ("La taille doit etre compris entre 1 et 3 ! ")
    self.orientation = orientation  # "H" (horizontal) ou "V" (vertical)
    if 0<=self.coordonnees_x<=5 :
      self.coordonees_x = coordonnees_x
    else : 
      print ("Les coordonnées doivent être compris entre 0 et 5 pour qu'elles puissent concorder avce le tableau !") 
    if 0<=self.coordonnees_y<=5 :
      self.coordonees_y = coordonnees_y
      print ("Les coordonnées doivent être compris entre 0 et 5 pour qu'elles puissent concorder avce le tableau !")
    if self.couleur == "rouge" : 
      self.couleur = couleur
      self.taille = 2
      self.symbole = "r"
      self.coordonnees_x = 2
      self.coordonnees_y = 0
    else : 
      self.couleur = couleur

    
  def avancer(self, nb_cases, plateau):
      """Déplace la voiture sur le plateau"""
      for i in range(self.taille):
          if self.orientation == "H":
              plateau.grille[self.coordonnees_x][self.coordonnees_y + i] = "x"
          else:
              plateau.grille[self.coordonnees_x + i][self.coordonnees_y] = "x"

        # 2. Mettre à jour les coordonnées
          if self.orientation == "H":
              self.coordonnees_y += nb_cases
          else:
              self.coordonnees_x += nb_cases

        # 3. Placer à la nouvelle position
          for i in range(self.taille):
              if self.orientation == "H":
                  plateau.grille[self.coordonnees_x][self.coordonnees_y + i] = self.symbole
              else:
                  plateau.grille[self.coordonnees_x + i][self.coordonnees_y] = self.symbole       


#plateau 

      taille = 6
      Plateau = []

      for ligne in range(taille):
          Plateau.append(["x"] * taille)

      for i in range(voiture.taille):
          Plateau[voiture.coordonnees_x][voiture.coordonnees_y + i] = self.symbole
      for ligne in range(taille):
          affichage = ""
          for colonne in range(taille):
              affichage += Plateau[ligne][colonne] + " "
          print(affichage)


