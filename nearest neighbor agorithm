from math import sqrt

def calculate_distance(x1, y1 , x2, y2):
    distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance   



def find_neighbor(current_xy , points , visited):
    shortest_distance = float("inf")
    neighbor = None
    for num, (x, y) in enumerate(points):
        if visited[num] is False:
            distance = calculate_distance(current_xy[0], current_xy[1], x, y)
            if distance < shortest_distance:
                shortest_distance = distance
                neighbor = num
    return shortest_distance , neighbor



def algorithm(points):
    current_point = 0
    path = []
    visited = [False] * len(points)
    visited[0] = True
    tot_distance = 0
    path.append(0)

    while len(path) < len(points):
        current_xy = points[current_point]
        distance , neighbor = find_neighbor(current_xy, points, visited)
        visited[neighbor] = True
        path.append(neighbor)
        tot_distance += distance
        current_point = neighbor
    
    zero_xy = points[0]
    tot_distance += calculate_distance(current_xy[0], current_xy[1], zero_xy[0], zero_xy[1])
    path.append(0)
    return path , tot_distance
