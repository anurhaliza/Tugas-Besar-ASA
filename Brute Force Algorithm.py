# Ajeng Nurhaliza Ar Rachman
# 24060121140109
# Program Algoritma Brute Force

import time

def calculate_distance(route, graph):
    distance = 0
    for i in range(len(route) - 1):
        current_node = route[i]
        next_node = route[i + 1]
        distance += graph[current_node][next_node]
    return distance

def brute_force_route(graph, start, end):
    nodes = list(graph.keys())
    permutations = get_permutations(nodes, start, end)

    shortest_route = None
    shortest_distance = float('inf')

    for permutation in permutations:
        route = list(permutation)
        distance = calculate_distance(route, graph)
        if distance < shortest_distance:
            shortest_route = route
            shortest_distance = distance
            print("Rute terdekat saat ini:", " -> ".join(shortest_route))
            print("Jarak saat ini:", shortest_distance)
            print("----------------------")

    return shortest_route, shortest_distance

def get_permutations(nodes, start, end):
    result = []
    visited = set()
    visited.add(start)
    current_path = [start]
    generate_permutations(nodes, start, end, visited, current_path, result)
    return result

def generate_permutations(nodes, start, end, visited, current_path, result):
    if start == end:
        result.append(tuple(current_path))
        return
    for node in nodes:
        if node not in visited and node in graph[start]:
            visited.add(node)
            current_path.append(node)
            generate_permutations(nodes, node, end, visited, current_path, result)
            current_path.pop()
            visited.remove(node)

# Graf
graph = {
    'A': {'B': 29, 'C': 5},
    'B': {'E': 28, 'F': 15, 'K': 27},
    'C': {'D': 21, 'E': 17},
    'D': {'H': 27, 'C': 21},
    'E': {'G': 10, 'B': 28, 'C': 17},
    'F': {'I': 9, 'G': 13, 'B': 15},
    'G': {'J': 11, 'H': 18, 'F': 13, 'E': 10},
    'H': {'P': 60},
    'I': {'K': 12, 'J': 16},
    'J': {'M': 13, 'I': 16},
    'K': {'L': 8},
    'L': {'M': 11, 'N': 6},
    'M': {'N': 12, 'L': 11},
    'N': {'O': 27},
    'O': {'P': 12},
    'P': {'Q': 10},
    'Q': {}
}

# Mencari rute terdekat
start_node = 'A'
end_node = 'Q'

start_time = time.time()
shortest_route, shortest_distance = brute_force_route(graph, start_node, end_node)
end_time = time.time()

if shortest_route is not None:
    print("PROGRAM ALGORITMA BRUTE FORCE")
    print("A: Stasiun Semarang Tawang")
    print("Q: Universitas Diponegoro")
    print("Rute terdekat dari", start_node, "ke", end_node, "adalah:", " -> ".join(shortest_route))
    print("Rincian Rute:")
    for i in range(len(shortest_route) - 1):
        current_node = shortest_route[i]
        next_node = shortest_route[i + 1]
        distance = graph[current_node][next_node]
        print("Dari", current_node, "ke", next_node, "jarak:", distance)
    print("Jarak antara Stasiun Semarang Tawang menuju Universitas Diponegoro:", shortest_distance)
    print("Waktu eksekusi:", end_time - start_time, "detik")
else:
    print("Tidak ada rute yang tersedia.")
