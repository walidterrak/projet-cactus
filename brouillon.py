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
    if nb_erreurs > 0:
        plt.plot(1, 0.7, 'ko', markersize=10)  # Tête
    if nb_erreurs > 1:
        plt.plot([1, 1], [0.6, 0.4], 'k')  # Corps
    if nb_erreurs > 2:
        plt.plot([0.9, 1], [0.55, 0.5], 'k')  # Bras gauche
    if nb_erreurs > 3:
        plt.plot([1, 1.1], [0.55, 0.5], 'k')  # Bras droit
    if nb_erreurs > 4:
        plt.plot([0.9, 1], [0.4, 0.3], 'k')  # Jambe gauche
    if nb_erreurs > 5:
        plt.plot([1, 1.1], [0.4, 0.3], 'k')  # Jambe droite

    # Paramètres d'affichage
    plt.axis('off')  # Cache les axes
    plt.xlim(-0.2, 1.4)  # Ajuste les limites de l'axe x
    plt.ylim(-0.2, 1.2)  # Ajuste les limites de l'axe y
    plt.show()  # Affiche le pendu

def choisir_mot():
    liste_mots = ["banane", "poire", "kiwi", "litchi", "pomme"]
    return random.choice(liste_mots)

# Initialisation du jeu
solution = choisir_mot()
tentatives = 8
lettres_trouvees = ""
mot_masque = "_" * len(solution)  # Mot masqué avec underscores

while tentatives > 0 and "_" in mot_masque:
    # Afficher l'état actuel du mot masqué et le nombre de tentatives restantes
    print(f"Mot à deviner : {mot_masque}")
    print(f"Tentatives restantes : {tentatives}")
    
    # Le joueur propose une lettre
    proposition_lettre = input("Proposez une lettre : ").lower()
    
    # Vérifier si la lettre est dans le mot
    if proposition_lettre in solution:
        lettres_trouvees += proposition_lettre
        
        # Mettre à jour le mot masqué
        mot_masque = "".join([lettre + " " if lettre in lettres_trouvees else "_ " for lettre in solution])
        print("Bien joué !")
    else:
        tentatives -= 1
        print("Erreur...")
        afficher_pendu(8 - tentatives)  # Afficher le pendu en fonction du nombre d'erreurs

# Fin de partie
if "_" not in mot_masque:
    print(f"Félicitations ! Vous avez trouvé le mot : {solution}")
else:
    print(f"Dommage ! Vous avez perdu. Le mot était : {solution}")

#Créer une liste de mots.
# Utiliser la fonction random.choice pour sélectionner un mot aléatoire.
# Créer une variable pour stocker le mot masqué (initialement, une chaîne de caractères composée de tirets _ de la même longueur que le mot).
#Boucle de jeu :

import random

def choisir_mot():

    liste_mots = ["banane", "poire", "kiwi", "litchi", "pomme" ]
    solution = print(random.choice(liste_mots))

affichage = ""
for l in solution:
  affichage = affichage + "_ "

# - compter le nombre de lettres
mot_masque = "_" * len(solution))

# - le joueur propose une lettre
proposition_lettre = input("Devine une lettre : ")

lettres_trouvees = ""

# - verifier si la lettre est dans le mot
if proposition_lettre in solution:
    tentatives = tentatives - 1

tentatives = 8



# - stocker le mot choisi aleatoirement

# - remplacer le nombre de lettres par  des tirets pour le mot masqué
# - creer un input et verifier que chaque lettre saisie correspond au mot masque
# -boucle while jusqu'a decompte à 0 ou apparition de toutes les lettres
# - verifier répétition des lettres
# - afficher la lettre au bon emplacement lors de sa saisie par l utilisateur 
# - si correspondance demasquée/ sinon enlevé une tentatives (decrementation du score
# -quand compte à 0 print du game over


 
    


    
'''
pyhton
Tant que le joueur n'a pas trouvé le mot et qu'il lui reste des tentatives :
#Afficher le mot masqué et le nombre de tentatives restantes.
#avec des étoiles ou des underscores. l* pen** ou l_ pen__
#Demander au joueur de deviner une lettre.
#Vérifier si la lettre est dans le mot :
#Si oui, mettre à jour le mot masqué en remplaçant les tirets correspondants.
#Si non, décrémenter le nombre de tentatives et afficher une partie du pendu.
#Fin de partie :

#Si le joueur a trouvé le mot, afficher un message de victoire.
#Sinon, afficher un message de défaite et révéler le mot.
'''


while True:
#     nb=  int(input("saisie d'un nombre positif:"))

#     # Vérifier si le nombre est positif
#     if nb > 0:
#         # Afficher tous les nombres de 1 jusqu'au nombre saisi
#         for i in range(1, nb + 1):
#             print(i)
#         break
#     else:
#             print("Erreur. le nb saisi n'est pas un entier positif.Veuillez recommencer")

import random
choix = ["casserole", "cuillere", "patate", "souris"]
solution = random.choice(choix)

solution = "casserole"
tentatives = 7
affichage = ""
lettres_trouvees = ""

for l in solution:
  affichage = affichage + "_ "

print(">> Bienvenue dans le pendu <<")

while tentatives > 0:
  print("\nMot à deviner : ", affichage)
  proposition = input("proposez une lettre : ")[0:1].lower()

  if proposition in solution:
      lettres_trouvees = lettres_trouvees + proposition
      print("-> Bien vu!")
  else:
    tentatives = tentatives - 1
    print("-> Nope\n")
    if tentatives==0:
        print(" ==========Y= ")
    if tentatives<=1:
        print(" ||/       |  ")
    if tentatives<=2:
        print(" ||        0  ")
    if tentatives<=3:
        print(" ||       /|\ ")
    if tentatives<=4:
        print(" ||       /|  ")
    if tentatives<=5:                    
        print("/||           ")
    if tentatives<=6:
        print("==============\n")

  affichage = ""
  for x in solution:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

  if "_" not in affichage:
      print(">>> Gagné! <<<")
      break
     
print("\n    * Fin de la partie *    ")