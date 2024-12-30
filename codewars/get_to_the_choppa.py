from collections import deque

def find_shortest_path(grid:list[list[Node]], start_node:Node, end_node:Node):
    if not grid or not start_node.passable or not end_node.passable:
        return []
    
    last_row, last_col = len(grid) - 1, len(grid[0]) - 1
    directions = ((1,0), (-1,0), (0,1), (0,-1))
    queue = deque([(start_node, [start_node])])
    visited = set([start_node])

    while queue:
        current_node, path = queue.popleft()

        if current_node == end_node:
            return path

        for dx, dy in directions:
            x, y = current_node.position.x + dx, current_node.position.y + dy

            if 0 <= x <= last_row and 0 <= y <= last_col and grid[x][y].passable:
                neighbor = grid[x][y]

                if neighbor not in visited:
                    queue.append(neighbor, path + [neighbor])
                    visited.add(neighbor)

    return []
