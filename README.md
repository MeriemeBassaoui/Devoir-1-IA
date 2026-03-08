# Algorithmes de Recherche dans un Labyrinthe (DFS, BFS, A*)

## Description

Ce devoir se base sur trois algorithmes de recherche (DFS, BFS, A*)pour résoudre un labyrinthe.  
Les algorithmes trouvent un chemin dans le labyrinthe entre : (S : départ  et G : objectif)
Les paramètres de labyrinthe: 
        - taille : 16 x 16
        - bordures et obstacles : '#'
        - départ : 'S'
        - objectif : 'G'
Un chemin entre S et G est garanti.

## Algorithmes utilisés
    ### DFS
    DFS utilise une pile **(stack)**
    - explore en profondeur un chemin avant de revenir en arrière
    - pas optimal, peut ne pas trouver le plus court chemin

    ### BFS
    BFS utilise une **file (queue)**
    - explore les noeuds niveau par niveau
    - optimal, peut garantir le plus court chemin

    ### A*
    A* utilise une **file de priorité** et une heuristique.
    Fonction utilisée : f(n) = g(n) + h(n)
        - g(n) : coût depuis le départ
        - h(n) : distance heuristique, heuristique utilisée : h(n) = |x1 - x2| + |y1 - y2| (distance de Manhattan)

## Structure du devoir
Devoir 1
- maze.py : génération du labyrinthe
- dfs.py : implémentation d'algorithme DFS
- bfs.py : implémentation d'algorithme BFS
- astar.py : implémentation d'algorithme A*
- main.py : point d'entrée principal

## Exécution 
Pour lancer le programme : exécuter main.py

## Résultats 
Le programme affiche le labyrinthe initial, l'exploration des algorithmes, le chemin solution et le tableau statistique
ci-dessous qui affiche les indicateurs de performances de chaque algorithme pour résoudre le labyrinthe. 

Algo     |  Temps(ms) | Explorés | Chemin
-----------------------------------------
DFS      |      0.429 |       82 |     69
BFS      |      1.380 |      144 |     27
A*       |      0.961 |      114 |     27

## Objectif
Projet réalisé dans le cadre d'un devoir du Cours **fondements d'intelligence artificielle**.



