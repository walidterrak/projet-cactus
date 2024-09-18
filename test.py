import random
import matplotlib.pyplot as plt

def afficher_pendu(nb_erreurs):
    """
    Affiche le pendu en fonction du nombre d'erreurs.
    """


    plt.figure()  # Crée une nouvelle figure


    # Dessine la potence
    plt.plot([0, 1], [0, 0], 'k')  # Base
    plt.plot([0.5, 0.5], [0, 1], 'k')  # Poteau vertical
    plt.plot([0.5, 1], [1, 1], 'k')  # Barre horizontale
    plt.plot([1, 1], [0.9, 0.8], 'k')  # Corde


    # Dessine le corps du pendu en fonction du nombre d'erreurs
    if nb_erreurs > 0:# Tête
    if nb_erreurs > 1:# Corps
    if nb_erreurs > 2:# Bras gauche
    if nb_erreurs > 3:# Bras droit
    if nb_erreurs > 4:# Jambe gauche
    if nb_erreurs > 5:# Jambe droite
    # Paramètres d'affichage
    plt.axis('off')  # Cache les axes
    plt.xlim(-0.2, 1.4)  # Ajuste les limites de l'axe x
    plt.ylim(-0.2, 1.2)  # Ajuste les limites de l'axe y
    plt.show()  # Affiche le pendu


def choisir_mot():
    liste_mots = ["banane", "poire", "kiwi", "litchi", "pomme" ]
    return random.choice(liste_mots)

solution = choisir_mot()
tentative = 8
lettres_trouvees = ""
proposition_lettre = input("Devine une lettre : ")
mot_masque = "_"* len(solution)

affichage = ""
for l in solution:
  affichage = affichage + "_ "


while tentatives>0:
   proposition_lettre = input("proposez une lettre : ")
   if proposition_lettre in solution:
      lettres_trouvees += proposition_lettre
      print("Bien jouer !")
    else :
     tentative -= 1
     print("erreur...")
     for i range(8 - tentative):
        print()



