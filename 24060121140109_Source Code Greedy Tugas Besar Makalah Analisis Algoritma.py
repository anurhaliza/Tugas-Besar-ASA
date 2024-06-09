# Ajeng Nurhaliza Ar Rachman
# 24060121140109
# Program Algoritma Greedy

import time

def greedy_route(graph, start, end):
    current_node = start
    visited = set()
    visited.add(start)
    route = [start]
    total_distance = 0

    while current_node != end:
        neighbors = graph[current_node]
        min_distance = float('inf')
        next_node = None

        for neighbor, distance in neighbors.items():
            if neighbor not in visited and distance < min_distance:
                min_distance = distance
                next_node = neighbor

        if next_node is None:
            return None, float('inf')

        route.append(next_node)
        visited.add(next_node)
        total_distance += min_distance
        current_node = next_node

        print("Langkah pengambilan keputusan")
        print("Titik awal:", current_node)
        print("Titik tujuan:", end)
        print("Pilihan tetangga:", neighbors)
        print("Jarak terpendek:", min_distance)
        print("Titik berikutnya:", next_node)
        print("Rute saat ini: {} ke {} adalah: {}".format(start, end, " -> ".join(route)))
        print("Jarak total:", total_distance)
        print("-----------------------------")

    return route, total_distance

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
    'L': {'M': 11, 'N': 9},
    'M': {'N': 12, 'L': 11},
    'N': {'O': 27},
    'O': {'P': 12},
    'P': {'Q': 10},
    'Q': {}
}

# Pencarian rute terdekat
start_node = 'A'
end_node = 'Q'

start_time = time.time()

shortest_route, shortest_distance = greedy_route(graph, start_node, end_node)

end_time = time.time()
execution_time = end_time - start_time

if shortest_route is not None:
    print("PROGRAM ALGORITMA GREEDY")
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
    print("Waktu eksekusi:", execution_time, "detik")
else:
    print("Tidak ada rute yang tersedia.")
