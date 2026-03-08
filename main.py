import time  
from maze import generate_maze, maze_marks, print_maze
from dfs import dfs
from bfs import bfs
from astar import astar 

def run_algo(name, alg, grid, start, goal): #Exécute un algorithme de recherche et mesure ses performances
    """ name  : nom de l'algorithme (DFS, BFS, A*)
        alg   : l'algorithme
        grid  : labyrinthe
        start : position de départ
        goal  : position objectif
    """

    t0 = time.perf_counter() # début du chronométrage
    path, explored, nodes_explored = alg(grid, start, goal) # exécution de l'algorithme
    t1 = time.perf_counter() # fin du chronométrage
    exec_time_ms = (t1 - t0) * 1000.0 # calcul du temps d'exécution en millisecondes
    path_len = len(path) if path else 0 # longueur du chemin trouvé

    return {
        "name": name,
        "path": path,
        "explored": explored,
        "nodes": nodes_explored,
        "time_ms": exec_time_ms,
        "path_len": path_len,
    } # retourner les résultats sous forme de dictionnaire


def print_results(res, grid): #Affiche les résultats d'un algorithme.
    print(f"\n===== {res['name']} =====")
    print(f"Chemin trouvé ? {'Oui' if res['path'] else 'Non'}")  # vérifier si un chemin a été trouvé
    print(f"Longueur du chemin: {res['path_len']}")  # longueur du chemin solution
    print(f"Temps d'exécution: {res['time_ms']:.3f} ms") # temps d'exécution
    print(f"Nb noeuds explorés: {res['nodes']}")  # nombre de noeuds explorés

    g2 = maze_marks(grid, explored=res["explored"], path=res["path"]) # créer une copie du labyrinthe avec marquage
    print("\nAffichage (p = exploration, * = solution):")
    print_maze(g2) # afficher le labyrinthe avec exploration et chemin


def print_statistique(all_results): #ffiche un tableau des performances des différents algorithmes.
    print("\n\n===== Tableau statistique =====")

    header = f"{'Algo':<8} | {'Temps(ms)':>10} | {'Explorés':>8} | {'Chemin':>6}" # en-tête du tableau
    print(header)
    print("-" * len(header))

    for r in all_results:
        print(f"{r['name']:<8} | {r['time_ms']:>10.3f} | {r['nodes']:>8} | {r['path_len']:>6}") # afficher les résultats de chaque algorithme


def main(): #Fonction principale du programme, génère le labyrinthe et exécute les algorithmes.
    size = 16       
    seed = 50       
    Mur_prob = 0.25 

    grid, start, goal = generate_maze(size=size, seed=seed, Mur_prob=Mur_prob) # génération du labyrinthe

    print("===== Labyrinthe initial =====")
    print_maze(grid) # affichage du labyrinthe initial
    print(f"\nDepart={start}, Objectif={goal}, seed={seed}, Mur_prob={Mur_prob}")  # affichage des paramètres
    
    results = [] # liste pour stocker les résultats

    for name, alg in [("DFS", dfs), ("BFS", bfs), ("A*", astar)]: # exécution des trois algorithmes
        res = run_algo(name, alg, grid, start, goal)
        results.append(res)  # sauvegarder les résultats
        print_results(res, grid) # afficher les résultats
    print_statistique(results) # afficher le tableau comparatif final

if __name__ == "__main__": # point d'entrée du programme
    main()