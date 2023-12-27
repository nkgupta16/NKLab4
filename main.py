def knapsack(items, max_size, mandatory_item_key=None):
    dp = [[0 for _ in range(max_size + 1)] for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        for w in range(1, max_size + 1):
            item_weight, item_value, item_key = items[i - 1]
            if item_weight <= w:
                if mandatory_item_key and item_key == mandatory_item_key and w == item_weight:
                    dp[i][w] = item_value
                else:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_weight] + item_value)
            else:
                dp[i][w] = dp[i - 1][w]
    return dp


def reconstruct_items(dp, items, max_size, mandatory_item_key=None):
    n = len(items)
    size = max_size
    taken = []
    for i in range(n, 0, -1):
        if dp[i][size] != dp[i - 1][size]:
            if mandatory_item_key and items[i - 1][2] == mandatory_item_key:
                continue
            taken.append(i - 1)
            size -= items[i - 1][0]
    return taken


def solve_backpack_problem(items, matrix_dimensions, disease, initial_points):
    global mandatory_item
    rows, cols = matrix_dimensions
    max_size = rows * cols
    items_list = [(items[key][0], items[key][1], key) for key in sorted(items)]

    # Cases of disease
    mandatory_item_key = None
    if disease == 'asthma':
        mandatory_item_key = 'i'
    elif disease == 'infection':
        mandatory_item_key = 'd'

    if mandatory_item_key:
        mandatory_item = items[mandatory_item_key]
        items_list = [item for item in items_list if item[2] != mandatory_item_key]
        max_size -= mandatory_item[0]
        initial_points += mandatory_item[1]

    dp = knapsack(items_list, max_size)
    taken = reconstruct_items(dp, items_list, max_size)

    result_matrix = [['' for _ in range(cols)] for _ in range(rows)]
    if mandatory_item_key:
        for _ in range(mandatory_item[0]):
            result_matrix[0][cols - mandatory_item[0] + _] = mandatory_item_key

    filled_cells = 0
    for index in taken:
        item_weight, _, item_key = items_list[index]
        placed = False
        for i in range(rows):
            for j in range(cols):
                if j + item_weight <= cols and all(result_matrix[i][k] == '' for k in range(j, j + item_weight)):
                    for k in range(item_weight):
                        result_matrix[i][j + k] = item_key
                    filled_cells += item_weight
                    placed = True
                    break
                elif i + item_weight <= rows and all(result_matrix[k][j] == '' for k in range(i, i + item_weight)):
                    for k in range(item_weight):
                        result_matrix[i + k][j] = item_key
                    filled_cells += item_weight
                    placed = True
                    break
            if placed:
                break

    if mandatory_item_key:
        filled_cells += mandatory_item[0]

    final_survival_points = initial_points + sum(items[cell][1] for row in result_matrix for cell in row if cell) - (
                max_size - filled_cells) * 5

    return result_matrix, final_survival_points


items = {
    'r': (3, 25),  # Rifle
    'p': (2, 15),  # Pistol
    'a': (2, 15),  # Ammo
    'm': (2, 20),  # Medkit
    'i': (1, 5),  # Inhaler
    'k': (1, 15),  # Knife
    'x': (3, 20),  # Axe
    't': (1, 25),  # Talisman (Amulet)
    'f': (1, 15),  # Flask
    'd': (1, 10),  # Antidote
    's': (2, 20),  # Supplies (Food)
    'c': (2, 20)  # Crossbow
}

options = [
    {'cells': (2, 4), 'disease': None, 'points': 15},
    {'cells': (3, 3), 'disease': 'asthma', 'points': 10},
    {'cells': (2, 4), 'disease': 'infection', 'points': 10},
    {'cells': (3, 3), 'disease': None, 'points': 15},
    {'cells': (2, 4), 'disease': 'asthma', 'points': 20},
    {'cells': (3, 3), 'disease': 'infection', 'points': 15},
    {'cells': (2, 4), 'disease': None, 'points': 15},
    {'cells': (3, 3), 'disease': 'asthma', 'points': 15},
    {'cells': (2, 4), 'disease': 'infection', 'points': 20},
    {'cells': (3, 3), 'disease': None, 'points': 10}
]

option_number = int(input("Enter option number (1-10): "))

if 1 <= option_number <= len(options):
    selected_option = options[option_number - 1]
    matrix_dimensions = selected_option['cells']
    disease = selected_option['disease']
    initial_points = selected_option['points']

    result_matrix, final_survival_points = solve_backpack_problem(items, matrix_dimensions, disease, initial_points)

    for row in result_matrix:
        print(' '.join([str(cell) if cell else '_' for cell in row]))
    print("Final Survival Points:", final_survival_points)
else:
    print("Invalid option number!")
