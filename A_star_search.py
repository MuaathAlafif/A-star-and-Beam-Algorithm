from queue import PriorityQueue
import math

def a_star_search_temperature(graph, start, goal, temperature_map):
    # Initialize open and closed sets
    open_set = PriorityQueue()
    open_set.put((0, start))
    
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = temperature_heuristic(start, goal, temperature_map)
    
    while not open_set.empty():
        current = open_set.get()[1]
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor] + temperature_map.get(neighbor, 0)
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + temperature_heuristic(neighbor, goal, temperature_map)
                
                open_set.put((f_score[neighbor], neighbor))
    
    return None

def temperature_heuristic(node, goal, temperature_map):
    # Custom heuristic that includes the effect of temperature
    distance = math.sqrt((node[0] - goal[0])**2 + (node[1] - goal[1])**2)
    temperature_penalty = temperature_map.get(node, 0)
    return distance + temperature_penalty

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

# Example 2D graph as a dictionary where each node has its neighbors with their respective costs
graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1, (0, 2): 1},
    (0, 2): {(0, 1): 1, (1, 2): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(1, 0): 1, (0, 1): 1, (1, 2): 1},
    (1, 2): {(1, 1): 1, (0, 2): 1},
}

# Temperature map for the environment (higher values mean more difficult traversal)
temperature_map = {
    (0, 0): 2,
    (0, 1): 1,
    (0, 2): 0.5,
    (1, 0): 1.5,
    (1, 1): 2.5,
    (1, 2): 1,
}

# Starting point and goal
start = (0, 0)
goal = (1, 2)

# Perform A* search
path = a_star_search_temperature(graph, start, goal, temperature_map)
print("Path found:", path)



#- temperature_map:تمثل هذه الخريطه درجة الحرارة الافتراضية أو "صعوبة" التنقل لكل عقدة. كلما كانت القيمة أعلى، زادت تكلفة المرور عبر تلك العقدة.

#- temperature_heuristic: هذه الدالة تستخدم لتقدير تكلفة الوصول من العقدة الحالية إلى الهدف، مع أخذ درجة الحرارة (أو صعوبة البيئة) في الاعتبار.

#- a_star_search_temperature:الخوارزمية الرئيسية التي تبحث عن أقصر مسار، مع مراعاة تأثير درجة الحرارة على المسار.



#1. يتم تخزين كل عقدة في الرسم البياني مع جيرانها وتكلفة الانتقال إليها.
#2. يتم تحديد درجة حرارة لكل عقدة تؤثر على تكلفة التنقل.
#3. تبدأ الخوارزمية من start وتبحث عن أقصر مسار للوصول إلى goal،
#مع أخذ تأثيرات درجة الحرارة في الحسبان.

#بهذه الطريقة يتم تقديم بعد جديد للبحث باستخدام A*.
#حيث تؤثر العوامل البيئية مثل درجة الحرارة أو الصعوبة على مسار البحث.