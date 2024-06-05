from math import sqrt, factorial
from random import randint
from time import sleep, time
import matplotlib.pyplot as plt
from itertools import permutations
from os import system

def brute_force(points):
    num_points = len(points)
    best_route = None
    best_distance = float("inf")
    for combinations in permutations(range(1, num_points)):
        route = [0] + list(combinations) + [0]
        distance = sum(calculate_distance(points[route[i]][0], points[route[i]][1], points[route[i + 1]][0], points[route[i + 1]][1]) for i in range(num_points))
        if distance < best_distance:
            best_distance = distance
            best_route = route
    return best_distance, best_route

def create_graph(points, route_alg, route_bf, bf):
    plt.figure(figsize=(10, 6))

    # Algorithm
    x_alg = [points[i][0] for i in route_alg]
    y_alg = [points[i][1] for i in route_alg]
    plt.plot(x_alg, y_alg, marker="o", color="b", label="Algorithm")

    if bf:
        # Brute force
        x_bf = [points[i][0] for i in route_bf]
        y_bf = [points[i][1] for i in route_bf]
        plt.plot(x_bf, y_bf, marker="o", color="r", linestyle="--", label="Brute Force")

    for i, (x, y) in enumerate(points):
        plt.text(x, y, f"{i}", fontsize=12, ha="right")

    plt.title("Routes")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.legend()
    plt.show()

def calculate_distance(x1, y1, x2, y2):
    distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance

def find_neighbor(current_xy, points, visited):
    shortest_distance = float("inf")
    nearest = None
    for num, (x, y) in enumerate(points):
        if not visited[num]:
            distance = calculate_distance(current_xy[0], current_xy[1], x, y)
            if distance < shortest_distance:
                shortest_distance = distance
                nearest = num
    return shortest_distance, nearest

def algorithm(points):
    current_point = 0
    route = []
    visited = [False] * len(points)
    visited[0] = True
    total_distance = 0
    route.append(0)

    while len(route) < len(points):
        current_xy = points[current_point]
        distance, nearest = find_neighbor(current_xy, points, visited)
        visited[nearest] = True
        route.append(nearest)
        total_distance += distance
        current_point = nearest

    zero_xy = points[0]
    total_distance += calculate_distance(current_xy[0], current_xy[1], zero_xy[0], zero_xy[1])
    route.append(0)
    return route, total_distance

def get_points(num, randomize):
    points = []
    count = 0

    while count < num:
        if randomize.lower() == "n":
            try:
                x = int(input(f"Enter coordinate {count}x: "))
                y = int(input(f"Enter coordinate {count}y: "))
            except ValueError:
                print("Invalid input, please enter integers.")
                return get_points(num, randomize)
        else:
            x = randint(0, 50)
            y = randint(0, 50)
        points.append((x, y))
        count += 1
    return points

def main():
    try:
        num_points = int(input("Enter number of points (max 10 if 'brute force' = y): "))
    except ValueError:
        print("Invalid input, please enter a number.")
        sleep(1)
        return

    if num_points <= 1:
        print(f"Enter at least 2 points. Added {2 - num_points} extra")
        num_points = 2

    brute_force_option = input("Brute force? (y/n): ")

    if brute_force_option.lower() not in ["y", "n", "force_y"]:
        print("Invalid input")
        sleep(1)
        return

    if brute_force_option.lower() == "y" and num_points > 10:
        print("Brute force supports a maximum of 10 points, removing excess points...")
        num_points = 10
        sleep(1)

    randomize = input("Randomize point coordinates? (y/n):")
    if randomize.lower() not in ["y", "n"]:
        print("Invalid input")
        sleep(1)
        return

    points = get_points(num_points, randomize)
    system("cls")

    start_time = time()
    route_algorithm, distance_algorithm = algorithm(points)
    end_time = time()

    print(f"Algorithm distance: {distance_algorithm}")
    print(f"Algorithm route: {route_algorithm}")
    print(f"Executed in: {end_time - start_time} seconds")

    if brute_force_option.lower() == "y" or brute_force_option.lower() == "force_y":
        start_time = time()
        distance_bf, route_bf = brute_force(points)
        end_time = time()
        print(f"\n\nBest distance: {distance_bf}")
        print(f"Best route: {route_bf}")

        if distance_algorithm > 0:  # Ensure not to divide by 0
            print(f"Distance difference: {distance_bf - distance_algorithm} ({(100 * (distance_bf - distance_algorithm)) / distance_algorithm}%)")
        else:
            print(f"Distance difference: {distance_bf - distance_algorithm} (-0%)")

        print(f"Executed in: {end_time - start_time} seconds")
        print(f"\n{factorial(len(points) - 1) / 2} possible combinations")
        create_graph(points, route_algorithm, route_bf, True)
    else:
        print(f"\n{factorial(len(points) - 1) / 2} possible combinations")
        create_graph(points, route_algorithm, [0], False)

main()
