import math

# Default heap example used by both the CLI and the Flask app.
DEFAULT_HEAP = [10, 20, 30, 35, 38, 40, 60]

def draw_heap(heap, vertical_gap=2):
    n = len(heap)
    if n == 0:
        return "Heap is empty"

    # Compute the height of the heap:
    height = math.floor(math.log2(n)) + 1

    # Compute maximum width among node strings.
    max_width = max(len(str(x)) for x in heap)
    cell_width = max_width + 1

    # Determine total grid width.
    total_slots = 2**height - 1
    total_width = total_slots * cell_width

    # Create a 2D grid for spaces.
    grid_height = height + (height - 1) * vertical_gap
    grid = [[' ' for _ in range(total_width)] for _ in range(grid_height)]

    # Helper: Draw a node string centered at the given column.
    def draw_node_str(row, col, node_str):
        for i, ch in enumerate(node_str):
            if 0 <= col + i < total_width:
                grid[row][col + i] = ch

    # Helper: Draw a diagonal edge from parent's center to child's center.
    def draw_edge_line(row_start, col_start, row_end, col_end):
        segments = row_end - row_start
        if segments <= 0:
            return
        for i in range(1, segments):
            row = row_start + i
            col = round(col_start + i * (col_end - col_start) / segments)
            grid[row][col] = '/' if col_end < col_start else '\\'

    # Place the node recursively.
    def place_node(index, level, left_bound, right_bound):
        if index > n or left_bound > right_bound:
            return

        node_row = level * (vertical_gap + 1)
        mid = (left_bound + right_bound) // 2
        node_str = str(heap[index - 1])
        node_str_width = len(node_str)
        node_col = mid - node_str_width // 2
        draw_node_str(node_row, node_col, node_str)
        parent_center = mid

        left_child = 2 * index
        right_child = 2 * index + 1
        next_level = level + 1
        child_row = next_level * (vertical_gap + 1)

        # Left child.
        if left_child <= n:
            child_left_bound = left_bound
            child_right_bound = mid - 1
            child_mid = (child_left_bound + child_right_bound) // 2 if child_left_bound <= child_right_bound else left_bound
            draw_edge_line(node_row, parent_center, child_row, child_mid)
            place_node(left_child, next_level, child_left_bound, mid - 1)

        # Right child.
        if right_child <= n:
            child_left_bound = mid + 1
            child_right_bound = right_bound
            child_mid = (child_left_bound + child_right_bound) // 2 if child_left_bound <= child_right_bound else right_bound
            draw_edge_line(node_row, parent_center, child_row, child_mid)
            place_node(right_child, next_level, mid + 1, right_bound)

    place_node(1, 0, 0, total_width - 1)
    return "\n".join("".join(row) for row in grid)

def main():
    tree_str = draw_heap(DEFAULT_HEAP)
    print(tree_str)

if __name__ == '__main__':
    main()
