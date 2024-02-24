# Application de Cartes Mémoire

## Présentation
Cette application de Cartes Mémoire est un projet Python développé avec le module Tkinter. Elle aide les utilisateurs à apprendre le vocabulaire français en présentant des cartes mémoire avec des mots français d'un côté et leur traduction en anglais de l'autre côté.

## Fonctionnalités
- Affichage des Cartes Mémoire : Les utilisateurs peuvent voir des mots français d'un côté de la carte mémoire et leurs traductions en anglais de l'autre côté.
- Apprentissage Interactif : Les utilisateurs peuvent indiquer s'ils ont correctement mémorisé la traduction ou non, permettant à l'application d'ajuster le contenu d'apprentissage en conséquence.
- Persistence : L'application enregistre la progression de l'utilisateur, garantissant aux utilisateurs de continuer là où ils se sont arrêtés.

## Fonctionnement
1. Visualisation des Cartes Mémoire : La méthode new_flashcard() affiche une nouvelle carte mémoire avec un mot français du fichier de données et déclenche un minuteur pour appeler la méthode show_answer après un délai.
2. Affichage de la Traduction : La méthode show_answer() permet d'afficher la traduction anglaise du mot français sur la carte mémoire.
3. Évaluation des Connaissances : Les utilisateurs peuvent cliquer sur des boutons indiquant s'ils ont correctement mémorisé la traduction ou non: le bouton rouge en cas d'échec, le bouton vert en cas de réussite.
4. Validation de la réponse correcte : La méthode got_right() permet de retirer la carte mémoire actuelle de la liste d'apprentissage si l'utilisateur déclare qu'il a correctement répondu, mettre à jour le fichier csv des mots restants à apprendre, et appelle de nouveau la méthode new_flashcard pour afficher une nouvelle carte.

## Installation et Configuration
- Python 3.9.6
- Bibliothèques requises : tkinter, pandas


## Aperçu de l'Interface
![Carte côté français](https://github.com/marionrobert/FlashCardApp/assets/107509668/78e2c533-b59b-4778-834b-e5657b45ecd1)
![Carte côré anglais](https://github.com/marionrobert/FlashCardApp/assets/107509668/9da0582c-e643-4554-a519-920c321f10e6)


## Remarques
Ce projet a été réalisé dans le cadre du cours [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) de Angela Yu sur la plateforme Udemy.
