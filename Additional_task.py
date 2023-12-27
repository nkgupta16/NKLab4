from itertools import combinations

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


def calculate_total(combination):
    total_size = sum(items[item][0] for item in combination)
    total_points = sum(items[item][1] for item in combination)
    return total_size, total_points


def find_combinations(items, max_size):
    all_combinations = []
    for i in range(1, len(items) + 1):
        for combo in combinations(items.keys(), i):
            size, points = calculate_total(combo)
            if size <= max_size and points > 0:
                all_combinations.append(combo)
    return all_combinations


max_inventory_size = 7
valid_combinations = find_combinations(items, max_inventory_size)

print(f"All valid combinations for an inventory of {max_inventory_size} cells for option 1:")
for combo in valid_combinations:
    print(f"Combination: {combo}, Total Points: {calculate_total(combo)[1]}")
