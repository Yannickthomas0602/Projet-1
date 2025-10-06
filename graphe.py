import random
import matplotlib.pyplot as plt

def lancer_de():
    """Simule un lancer de dé et renvoie le résultat (1 à 6)."""
    return random.randint(1, 6)

def simulation(nb_lancers):
    """Simule plusieurs lancers et renvoie la fréquence de chaque face."""
    resultats = [0] * 6  # liste pour compter les faces 1 à 6

    for _ in range(nb_lancers):
        face = lancer_de()
        resultats[face - 1] += 1

    return resultats

def afficher_graphe(resultats):
    """Affiche un histogramme des résultats."""
    faces = [1, 2, 3, 4, 5, 6]
    plt.bar(faces, resultats)
    plt.title("Résultats des lancers de dé")
    plt.xlabel("Face du dé")
    plt.ylabel("Nombre d'occurrences")
    plt.show()

# Programme principal
if __name__ == "__main__":
    nb_lancers = int(input("Combien de fois veux-tu lancer le dé ? "))
    resultats = simulation(nb_lancers)
    print("Résultats :", resultats)
    afficher_graphe(resultats)
