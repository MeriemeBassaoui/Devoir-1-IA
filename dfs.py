from collections import deque
from maze import voisins, depart, objectif


def reconstruct_path(parent, start, goal): #Reconstruit le chemin trouvé entre le départ et l'objectif.
    """parent : dictionnaire qui stocke le parent de chaque noeud
        start  : position de départ
        goal   : position objectif
        On remonte depuis goal jusqu'à start en suivant les parents.
    """

    # Si l'objectif n'a jamais été atteint
    if goal not in parent and goal != start:
        return None

    cur = goal           # on commence par l'objectif
    path = [cur]         # la liste du chemin commence par goal

    # On remonte jusqu'au départ
    while cur != start:
        cur = parent[cur]  # on récupère le parent du noeud courant
        path.append(cur)   # on ajoute ce noeud au chemin

    # Le chemin est inversé (goal -> start), donc on le renverse
    path.reverse()

    return path


def dfs(grid, start, goal): #Implémentation de DFS
    """
    grid  : labyrinthe
    start : position de départ
    goal  : position objectif
    """

    # Pile utilisée pour DFS (structure LIFO)
    stack = [start]

    # Ensemble des noeuds déjà visités
    visited = set([start])

    # Dictionnaire pour mémoriser le parent de chaque noeud
    parent = {}

    # Liste des noeuds explorés (utilisée pour affichage)
    explored_order = []

    # Compteur de noeuds explorés
    nodes_explored = 0

    # Boucle principale de recherche
    while stack:

        # On retire le dernier élément de la pile
        cur = stack.pop()

        # On incrémente le nombre de noeuds explorés
        nodes_explored += 1

        # On ajoute le noeud à la liste d'exploration
        explored_order.append(cur)

        # Si on atteint l'objectif, on arrête la recherche
        if cur == goal:
            break

        # Explorer les voisins du noeud courant
        for nb in voisins(grid, cur):

            # Si le voisin n'a pas encore été visité
            if nb not in visited:

                visited.add(nb)      # marquer comme visité
                parent[nb] = cur     # enregistrer son parent
                stack.append(nb)     # ajouter dans la pile

    # Reconstruction du chemin solution
    path = reconstruct_path(parent, start, goal)

    # Conversion de la liste des noeuds explorés en ensemble
    explored_set = set(explored_order)

    return path, explored_set, nodes_explored 

    