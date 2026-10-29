regions = ['A', 'B', 'C', 'D']

colors = ['Red', 'Green', 'Blue']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

assignment = {}

def is_valid(region, color):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve():
    if len(assignment) == len(regions):
        return True

    region = next(r for r in regions if r not in assignment)

    for color in colors:
        if is_valid(region, color):
            assignment[region] = color
            if solve():
                return True
            del assignment[region]

    return False

if solve():
    print("Color Mapping:")
    for region in regions:
        print(region, "->", assignment[region])
else:
    print("No solution exists.")