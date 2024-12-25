
def enqueue(queue, node):
    queue.append(node)

def dequeue(queue):
    return queue.pop()


def bfs(graph, start_node):
    visited = set()         
    queue = []               
    bfs_traversal = []      

    enqueue(queue, start_node)  

    while queue:
        current_node = dequeue(queue) 

        if current_node not in visited:
            visited.add(current_node)  
            bfs_traversal.append(current_node)  

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    enqueue(queue, neighbor)

    return bfs_traversal

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2, 6],
    6: [3, 5]
}

start_node = 1
print("BFS Traversal:", bfs(graph, start_node))
