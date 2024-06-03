from math import sqrt , factorial
from random import randint
from  time import sleep , time
import matplotlib.pyplot as plt
from itertools import permutations
from os import system



def forza_bruta(punti):
    num_punti = len(punti)
    miglior_percorso = None
    miglior_distanza = float("inf")
    for combinazioni in permutations(range(1 , num_punti)):
        percorso = [0] + list(combinazioni) + [0]
        distanza = sum(calcolo_distanza(punti[percorso[i]][0], punti[percorso[i]][1], punti[percorso[i + 1 ]][0], punti[percorso[i + 1 ]][1]) for i in range(num_punti))
        if distanza < miglior_distanza:
            miglior_distanza = distanza
            miglior_percorso = percorso
    return miglior_distanza , miglior_percorso
    
    

def crea_grafico(punti, percorso_alg, percorso_bf, bf):
    plt.figure(figsize = (10, 6))

    #algoritmo
    x_alg = [punti[i][0] for i in percorso_alg]
    y_alg = [punti[i][1] for i in percorso_alg]
    plt.plot(x_alg, y_alg, marker="o", color="b", label="Algoritmo")

    if bf:
    #forza bruta
        x_bf = [punti[i][0] for i in percorso_bf]
        y_bf = [punti[i][1] for i in percorso_bf]
        plt.plot(x_bf, y_bf, marker="o", color="r", linestyle="--", label="Brute Force")

    for i, (x, y) in enumerate(punti):
        plt.text(x, y, f"{i}", fontsize=12, ha="right")

    plt.title("Percorsi")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.legend()
    plt.show()



def calcolo_distanza(x1, y1 , x2, y2):
    distanza = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distanza    



def trova_vicino(xy_correnti , punti , visitati):
    distanza_corta = float("inf")
    vicino = None
    for num, (x, y) in enumerate(punti):
        if visitati[num] is False:
            distanza = calcolo_distanza(xy_correnti[0], xy_correnti[1], x, y)
            if distanza < distanza_corta:
                distanza_corta = distanza
                vicino = num
    return distanza_corta , vicino



def algoritmo(punti):
    punto_corrente = 0
    percorso = []
    visitati = [False] * len(punti)
    visitati[0] = True
    tot_distanza = 0
    percorso.append(0)

    while len(percorso) < len(punti):
        xy_correnti = punti[punto_corrente]
        distanza , vicino = trova_vicino(xy_correnti, punti, visitati)
        visitati[vicino] = True
        percorso.append(vicino)
        tot_distanza += distanza
        punto_corrente = vicino
    
    zero_xy = punti[0]
    tot_distanza += calcolo_distanza(xy_correnti[0], xy_correnti[1], zero_xy[0], zero_xy[1])
    percorso.append(0)
    return percorso , tot_distanza




def prendi_punti(num, randomizza):
    punti = []
    conto = 0

    while conto < num:

        if randomizza.lower() == "n":
            try:
                x = int(input(f"inserisci coordinata {conto}x: "))
                y = int(input(f"inserisci coordinata {conto}y: "))
            except ValueError:
                print("Input invalido, inserire numeri interi.")
                return prendi_punti(num , randomizza)
        else:
            x = randint(0 , 50)
            y = randint(0 , 50)
        punti.append((x, y))
        conto += 1
    return punti



def main():
    try:
        num_punti = int(input("inserisci numero di punti (max 10 se 'brute force' = y): "))
    except ValueError:
        print("input invalido, inserire un numero.")
        sleep(1)
        return
    
    if num_punti <= 1:
        print(f"inserire almeno 2 punti. inseriti {2 - num_punti} extra")
        num_punti = 2
        
    brute_force = input("Brute force? (y/n): ")

    if brute_force.lower() not in ["y", "n", "force_y"]:
        print("input invalido")
        sleep(1)
        return
    
    if brute_force.lower() == "y" and num_punti > 10:
        print("Brute force supporta un massimo di 10 punti, Eliminando punti in eccesso...")
        num_punti = 10
        sleep(1)
    
    randomizza = input("Randomizzare coordinate punti? (y/n):")
    if randomizza.lower() not in ["y", "n"]:
        print("input invalido")
        sleep(1)
        return

    punti = prendi_punti(num_punti , randomizza)
    system("cls")

    tempo_inizio = time()
    percorso_algoritmo , distanza_algoritmo = algoritmo(punti)
    tempo_fine = time()
    
    print(f"Distanza algoritmo: {distanza_algoritmo}")
    print(f"Percorso algoritmo: {percorso_algoritmo}")
    print(f"eseguito in: {tempo_fine - tempo_inizio} secondi")
    
    if brute_force.lower() == "y" or brute_force.lower() == "forza_y":
        tempo_inizio = time()
        distanza_fb , percorso_fb = forza_bruta(punti)
        tempo_fine = time()
        print(f"\n\nDistanza migliore: {distanza_fb}")
        print(f"Percorso migliore: {percorso_fb}")

        if distanza_algoritmo > 0: #assicura di non dividere per 0
            print(f"differenza distanze: {distanza_fb - distanza_algoritmo} ({(100* (distanza_fb - distanza_algoritmo)) / distanza_algoritmo}%)")
        else:
            print(f"differenza distanze: {distanza_fb - distanza_algoritmo} (-0%)")
        
        print(f"eseguito in: {tempo_fine - tempo_inizio} secondi")
        print(f"\n{factorial(len(punti) - 1 )/2} possibili combinazioni")
        crea_grafico(punti, percorso_algoritmo, percorso_fb, True)
    else:
        print(f"\n{factorial(len(punti) - 1 )/2} possibili combinazioni")
        crea_grafico(punti , percorso_algoritmo , [0], False)
    
    
main()
