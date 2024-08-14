import heapq

def beam_search(graph, start, goal, beam_width):
    """
    Perform Beam Search on a graph.
    
    :param graph: A dictionary where keys are nodes and values are lists of (neighbor, cost) tuples.
    :param start: The start node.
    :param goal: The goal node.
    :param beam_width: The number of beams to keep at each level.
    :return: A path from start to goal if found, otherwise None.
    """
    # Priority queue for beam search
    frontier = [(0, start, [])]  # (cost, current_node, path)
    visited = set()
    
    while frontier:
        # Extract the top beams based on cost
        new_frontier = []
        for _ in range(beam_width):
            if not frontier:
                break
            cost, current, path = heapq.heappop(frontier)
            if current in visited:
                continue
            visited.add(current)
            new_path = path + [current]
            if current == goal:
                return new_path
            for neighbor, edge_cost in graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(new_frontier, (cost + edge_cost, neighbor, new_path))
        frontier = heapq.nlargest(beam_width, new_frontier)
    
    return None

# Example graph representation
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('F', 1)],
    'E': [('F', 2)],
    'F': []
}

start_node = 'A'
goal_node = 'F'
beam_width = 2

path = beam_search(graph, start_node, goal_node, beam_width)
print("Path found:", path)



#- graph: يمثل الرسم البياني حيث يكون كل مفتاح هو عقدة، والقيمة هي قائمة من الأزواج (الجيران، التكلفة).
#- beam_width: عدد المسارات التي نحتفظ بها في كل مستوى.
#- frontier: قائمة تحتوي على العناصر التي سيتم فحصها، مرتبة حسب التكلفة. نستخدم هنا heapq لفرز العناصر حسب التكلفة.
#- visited: مجموعة تتعقب العقد التي تم زيارتها بالفعل لتجنب التكرار.