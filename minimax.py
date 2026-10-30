def minimax(depth, node, maximizingPlayer, values):
    if depth == 0:
        return values[node]
    if maximizingPlayer:
        return max(
            minimax(depth - 1, node * 2, False, values),
            minimax(depth - 1, node * 2 + 1, False, values)
        )
    else:
        return min(
            minimax(depth - 1, node * 2, True, values),
            minimax(depth - 1, node * 2 + 1, True, values)
        )

print("Minimax Algorithm")
values = list(map(int, input("Enter 8 leaf node values separated by spaces: ").split()))
if len(values) != 8:
    print("Please enter exactly 8 values.")
else:
    result = minimax(3, 0, True, values)
    print("\nLeaf values:", values)
    print("Best value:", result)