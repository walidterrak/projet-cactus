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