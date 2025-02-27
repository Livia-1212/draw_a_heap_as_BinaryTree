import math

def draw_heap(heap, vertical_gap=2):
    n = len(heap)
    if n == 0:
        print("Heap is empty")
        return

    # 1. Compute the height of the heap:
    height = math.floor(math.log2(n)) + 1

    # Compute the maximum width among node strings.
    max_width = max(len(str(x)) for x in heap)
    # We'll use a cell width that is the node width plus some padding.
    cell_width = max_width + 1

    # 2. Determine total grid width.
    # A complete binary tree has 2^height - 1 slots. Each slot has width = cell_width.
    total_slots = 2**height - 1
    total_width = total_slots * cell_width

    # Total grid height: one row per level for nodes plus vertical_gap rows between levels.
    grid_height = height + (height - 1) * vertical_gap
    grid = [[' ' for _ in range(total_width)] for _ in range(grid_height)]

    # Helper function to draw a node string centered at a given column.
    def draw_node_str(row, col, node_str):
        for i, ch in enumerate(node_str):
            if 0 <= col + i < total_width:
                grid[row][col + i] = ch

    # Helper function to draw a diagonal line from (row_start, col_start) to (row_end, col_end).
    # This uses linear interpolation over the vertical gap.
    def draw_edge_line(row_start, col_start, row_end, col_end):
        segments = row_end - row_start
        if segments <= 0:
            return
        for i in range(1, segments):
            row = row_start + i
            # Linear interpolation for the column position.
            col = round(col_start + i * (col_end - col_start) / segments)
            # Choose the edge character based on the direction.
            if col_end < col_start:
                grid[row][col] = '/'
            else:
                grid[row][col] = '\\'

    # Recursive function to place nodes and draw edges.
    # left_bound and right_bound define the horizontal region (in character indices) allotted to this subtree.
    def place_node(index, level, left_bound, right_bound):
        if index > n or left_bound > right_bound:
            return

        # Compute the row where the node will be placed.
        node_row = level * (vertical_gap + 1)
        # Determine the middle of the allotted region.
        mid = (left_bound + right_bound) // 2
        # Center the node string at 'mid'.
        node_str = str(heap[index - 1])
        node_str_width = len(node_str)
        node_col = mid - node_str_width // 2
        draw_node_str(node_row, node_col, node_str)
        parent_center = mid  # parent's center column

        left_child = 2 * index
        right_child = 2 * index + 1
        next_level = level + 1
        child_row = next_level * (vertical_gap + 1)

        # For left child.
        if left_child <= n:
            # Allot the left region: from left_bound to (mid - 1)
            child_left_bound = left_bound
            child_right_bound = mid - 1
            # Compute child's center; if the region is invalid, default to left_bound.
            child_mid = (child_left_bound + child_right_bound) // 2 if child_left_bound <= child_right_bound else left_bound
            # Draw the edge from parent's center to child's center.
            draw_edge_line(node_row, parent_center, child_row, child_mid)
            # Recurse for left child.
            place_node(left_child, next_level, child_left_bound, mid - 1)

        # For right child.
        if right_child <= n:
            # Allot the right region: from (mid + 1) to right_bound.
            child_left_bound = mid + 1
            child_right_bound = right_bound
            child_mid = (child_left_bound + child_right_bound) // 2 if child_left_bound <= child_right_bound else right_bound
            draw_edge_line(node_row, parent_center, child_row, child_mid)
            place_node(right_child, next_level, mid + 1, right_bound)

    # 4. Place the root node (index 1) using the full width.
    place_node(1, 0, 0, total_width - 1)

    # 7. Print the grid row by row.
    for row in grid:
        print("".join(row))

# Example usage:
heap1 = [10, 15, 20, 17, 25, 30, 35, 40, 45, 50]
heap2 = [10, 20, 30, 35, 38, 40, 60]
draw_heap(heap1)
draw_heap(heap2)
