import random

Mur = "#"        # un mur ou obstacle
Passage = "."    # un passage libre
depart = "S"     # position de départ
objectif = "G"   # position de l'objectif

# Ordre des directions pour explorer les voisins (Droite, Bas, Gauche, Haut)
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (dr, dc) r: ligne et c: colonne 

def generate_maze(size=16, seed=None, Mur_prob=0.25): #Génère un labyrinthe carré de taille size x size.
    """ size (int): Taille du labyrinthe (par défaut 16x16)
        seed (int) : Graine aléatoire pour générer toujours le même labyrinthe
        Mur_prob (float): Probabilité de placer un mur dans une case libre"""

    if size < 4: # Vérifie que la taille est valide
        raise ValueError("size doit être >= 4")

    if not (0.0 <= Mur_prob <= 1.0): # Vérifie que la probabilité est valide
        raise ValueError("Mur_prob doit être entre 0 et 1")

    rng = random.Random(seed) # Générateur aléatoire avec seed 

    # Création d'une grille remplie de murs
    grid = [[Mur for _ in range(size)] for _ in range(size)]

    # Les cases intérieures deviennent libres et les bords restent des murs
    for r in range(1, size - 1):
        for c in range(1, size - 1):
            grid[r][c] = Passage

    # Position de départ et objectif
    sr, sc = 1, 1
    gr, gc = size - 2, size - 2

    # Construire un chemin garanti entre S et G
    r, c = sr, sc

    # Ensemble des cases appartenant au chemin garanti
    path_cells = {(r, c)}

    # Nombre de déplacements nécessaires (Droite pour atteindre la colonne de G et Bas pour atteindre la ligne de G)
    moves = ["R"] * (gc - sc) + ["D"] * (gr - sr)

    # Mélange aléatoire des mouvements
    rng.shuffle(moves)

    # Construction du chemin
    for m in moves:
        if m == "R":
            c += 1
        else:
            r += 1
        path_cells.add((r, c))

    # Ajout des murs aléatoires
    for r in range(1, size - 1):
        for c in range(1, size - 1):

            # ne pas modifier les cases du chemin
            if (r, c) in path_cells or (r, c) in [(sr, sc), (gr, gc)]:
                continue

            # placer un mur avec une certaine probabilité
            if rng.random() < Mur_prob:
                grid[r][c] = Mur

    # Placer S et G
    grid[sr][sc] = depart
    grid[gr][gc] = objectif

    # Retourne le labyrinthe et les positions
    return grid, (sr, sc), (gr, gc)


def voisins(grid, pos): #Retourne les voisins accessibles d'une case.

    n = len(grid)
    r, c = pos

    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc

        # Vérifie que la cases est dans la grille et que ce n'est pas un mur
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != Mur:
            yield (nr, nc)


def print_maze(grid): #Affiche le labyrinthe de manière lisible.
    print("\n".join(" ".join(row) for row in grid))


def maze_marks(grid, explored=None, path=None): #Retourne une copie du labyrinthe avec : (p : noeuds explorées, * : chemin solution)
    # copie de la grille originale
    g = [row[:] for row in grid]

    # marquer les noueuds explorées
    if explored:
        for (r, c) in explored:
            if g[r][c] not in (depart, objectif):
                g[r][c] = "p"

    # marquer le chemin final
    if path:
        for (r, c) in path:
            if g[r][c] not in (depart, objectif):
                g[r][c] = "*"

    return g