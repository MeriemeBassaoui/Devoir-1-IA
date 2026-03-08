import heapq
from maze import voisins


def manhattan(a, b):
    """
    Calcule la distance de Manhattan entre deux cases.
    Cette heuristique est utilisée par A* pour estimer la distance entre une case et l'objectif.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def reconstruct_path(parent, start, goal): #Reconstruit le chemin trouvé entre le départ et l'objectif
    """On remonte depuis goal jusqu'à start en suivant les parents."""
    # Si l'objectif n'a jamais été atteint
    if goal not in parent and goal != start:
        return None

    cur = goal
    path = [cur]

    # Remonter les parents jusqu'au départ
    while cur != start:
        cur = parent[cur]
        path.append(cur)

    # Inverser le chemin (car il est construit à l'envers)
    path.reverse()

    return path


def astar(grid, start, goal): #Implémentation de l'algorithme A*
    """
    A* combine :
    - le coût réel depuis le départ : g(n)
    - une estimation du coût jusqu'à l'objectif : h(n)
    Fonction utilisée : f(n) = g(n) + h(n)
    """

    # File de priorité (min-heap)
    heap = []

    # Dictionnaire du coût réel depuis le départ
    g_cost = {start: 0}

    # Dictionnaire des parents pour reconstruire le chemin
    parent = {}

    # Ensemble des noeuds déjà visités
    visited = set()

    # Ajouter le noeud de départ dans le heap
    # (f, tie, node)
    # tie sert à départager les noeuds ayant le même f
    heapq.heappush(heap, (manhattan(start, goal), 0, start))

    # Liste des noeuds explorés
    explored_order = []

    # Compteur de noeuds explorés
    nodes_explored = 0

    # Compteur utilisé pour départager les noeuds dans le heap
    tie_counter = 0

    # Boucle principale de l'algorithme
    while heap:

        # Extraire le noeud avec le plus petit f(n)
        f, _, cur = heapq.heappop(heap)

        # Si le noeud a déjà été visité, on l'ignore
        if cur in visited:
            continue

        visited.add(cur)

        # Mise à jour du nombre de noeuds explorés
        nodes_explored += 1

        # Ajouter ce noeud à la liste explorée
        explored_order.append(cur)

        # Si on atteint l'objectif, on arrête
        if cur == goal:
            break

        # Explorer les voisins du noeud courant
        for nb in voisins(grid, cur):

            # Calcul du nouveau coût g(n)
            tentative_g = g_cost[cur] + 1

            # Si le voisin n'a pas encore été exploré
            # ou si on trouve un chemin moins coûteux
            if nb not in g_cost or tentative_g < g_cost[nb]:

                # Mise à jour du coût
                g_cost[nb] = tentative_g

                # Enregistrer le parent
                parent[nb] = cur

                # Incrément du compteur de priorité
                tie_counter += 1

                # Calcul de f(n) = g(n) + h(n)
                f_score = tentative_g + manhattan(nb, goal)

                # Ajouter dans la file de priorité
                heapq.heappush(heap, (f_score, tie_counter, nb))

    # Reconstruction du chemin solution
    path = reconstruct_path(parent, start, goal)

    # Ensemble des noeuds explorés
    explored_set = set(explored_order)

    return path, explored_set, nodes_explored