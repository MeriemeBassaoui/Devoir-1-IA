from collections import deque
from maze import voisins


def reconstruct_path(parent, start, goal): #Reconstruit le chemin entre le départ et l'objectif.
    
    """On remonte depuis l'objectif jusqu'au départ, en suivant les parents des noeuds."""

    # Si l'objectif n'a jamais été atteint
    if goal not in parent and goal != start:
        return None

    cur = goal          # on commence par l'objectif
    path = [cur]        # la liste du chemin commence avec goal

    # Remonter les parents jusqu'au départ
    while cur != start:
        cur = parent[cur]
        path.append(cur)

    # Inverser le chemin (car on l'a construit à l'envers)
    path.reverse()

    return path


def bfs(grid, start, goal): #Implémentation de BFS

    # File utilisée pour BFS FIFO
    q = deque([start])

    # Ensemble des noeuds déjà visités
    visited = set([start])

    # Dictionnaire qui stocke le parent de chaque noeud
    parent = {}

    # Liste des noeuds explorés (utile pour l'affichage)
    explored_order = []

    # Compteur du nombre de noeuds explorés
    nodes_explored = 0

    # Boucle principale de recherche
    while q:

        # Retirer le premier élément de la file
        cur = q.popleft()

        # Incrémenter le compteur de noeuds explorés
        nodes_explored += 1

        # Ajouter ce noeud à la liste des noeuds explorés
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
                q.append(nb)         # ajouter à la file

    # Reconstruction du chemin solution
    path = reconstruct_path(parent, start, goal)

    # Conversion en ensemble pour l'affichage
    explored_set = set(explored_order)

    return path, explored_set, nodes_explored