import heapq
import collections
from typing import Dict, List, Tuple


def dijkstra(
    graph: Dict[str, List[Tuple[str, int]]],
    start: str,
    end: str
) -> int:
    """
    Finds the shortest distance between two vertices in a graph.

    Args:
        graph: Graph represented as adjacency lists
        start: Starting vertex
        end: Target vertex

    Returns:
        int: Shortest distance or -1 if path not found
    """
    distances: Dict[str, float] = {city: float('inf') for city in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_dist, current_city = heapq.heappop(priority_queue)

        if current_dist > distances[current_city]:
            continue

        if current_city == end:
            return int(current_dist)

        for neighbor, weight in graph[current_city]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return -1


def shortest() -> None:
    """
    Determines the shortest distance between two settlements.

    The function reads:
    - N - number of settlements
    - M - number of roads
    - M lines with road information (settlement1 settlement2 distance)
    - Two settlements to find the path between

    Prints the shortest distance between them.
    """
    n = int(input("Enter the number of settlements: "))
    m = int(input("Enter the number of roads: "))

    graph = collections.defaultdict(list)

    print("Enter road information (settlement1 settlement2 distance):")
    for _ in range(m):
        city1, city2, dist = input().split()
        dist = int(dist)
        graph[city1].append((city2, dist))
        graph[city2].append((city1, dist))

    start, end = input("Enter start and end settlements: ").split()

    result = dijkstra(graph, start, end)

    if result != -1:
        print(f"Shortest distance between {start} and {end}: {result}")
    else:
        print(f"Path between {start} and {end} not found")


if __name__ == "__main__":
    shortest()
