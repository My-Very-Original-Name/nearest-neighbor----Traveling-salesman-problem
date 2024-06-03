from math import sqrt

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
