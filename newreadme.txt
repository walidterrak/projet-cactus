# Jeu du Pendu

## Description

Ce projet implémente un jeu classique du **Pendu** en Python. Le joueur doit deviner un mot secret, lettre par lettre, avant d'épuiser toutes ses tentatives. À chaque erreur, une partie du pendu est affichée. Le but est de deviner le mot complet avant que le pendu ne soit entièrement dessiné.

Ce projet utilise :
- **random** pour choisir un mot aléatoirement.
- **matplotlib** pour afficher le pendu graphiquement.
- Des concepts fondamentaux de programmation tels que les boucles, conditions, et manipulation de chaînes de caractères.

## Fonctionnalités

- **Choix aléatoire d'un mot** : Le programme sélectionne un mot aléatoirement dans une liste prédéfinie de mots.
- **Affichage du pendu** : À chaque tentative incorrecte, une partie du pendu est affichée graphiquement à l'aide de `matplotlib`.
- **Gestion des erreurs** : Le jeu compte le nombre de tentatives restantes. Une erreur fait apparaître une partie du pendu.
- **Victoire/Défaite** : Le joueur gagne s'il devine toutes les lettres avant d'épuiser ses tentatives. Sinon, le joueur perd et le mot est révélé.

## Prérequis

Avant de lancer le jeu, vous devez avoir :
- **Python 3.x** installé sur votre machine.
- **matplotlib** pour l'affichage graphique du pendu. Si vous ne l'avez pas, installez-la avec la commande suivante :
  ```bash
  pip install matplotlib