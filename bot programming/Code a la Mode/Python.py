import sys
import math
from collections import deque

KITCHEN_WIDTH = 11
KITCHEN_HEIGHT = 7
KITCHEN_MAP = []
CUSTOMER_ORDERS = []
EQUIPMENT_LOCATIONS = {}
ITEM_LOCATIONS = {}
ALL_TABLES = []
INGREDIENTS_NEEDED = ["BLUEBERRIES", "ICE_CREAM"]

def initialize_game_data():
    global KITCHEN_MAP, CUSTOMER_ORDERS, EQUIPMENT_LOCATIONS, ITEM_LOCATIONS, ALL_TABLES

    try:
        num_all_customers = int(sys.stdin.readline())
    except:
        num_all_customers = 0
        
    for _ in range(num_all_customers):
        try:
            inputs = sys.stdin.readline().split()
            customer_item = inputs[0]
            customer_award = int(inputs[1])
            CUSTOMER_ORDERS.append((customer_item, customer_award))
        except:
            pass

    for y in range(KITCHEN_HEIGHT):
        try:
            kitchen_line = sys.stdin.readline().strip()
            KITCHEN_MAP.append(kitchen_line)
            for x in range(KITCHEN_WIDTH):
                char = kitchen_line[x]
                if char in "DWI":
                    EQUIPMENT_LOCATIONS[char] = (x, y)
                elif char == 'B':
                    ITEM_LOCATIONS['B'] = (x, y)
                elif char == '#':
                    ALL_TABLES.append((x, y))
        except:
            KITCHEN_MAP.append("." * KITCHEN_WIDTH)

initialize_game_data()

def is_valid_position(x, y):
    return 0 <= x < KITCHEN_WIDTH and 0 <= y < KITCHEN_HEIGHT and KITCHEN_MAP[y][x] != "#"

def get_target_adjacent_position(start_x, start_y, target_x, target_y, partner_pos):
    queue = deque([[(start_x, start_y)]])
    visited = set([(start_x, start_y)])
    
    while queue:
        path = queue.popleft()
        x, y = path[-1]

        dx_target = abs(x - target_x)
        dy_target = abs(y - target_y)
        if max(dx_target, dy_target) == 1:
            return path
        
        if len(path) > 15:
            continue

        for move_x, move_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + move_x, y + move_y
            
            if is_valid_position(next_x, next_y) and (next_x, next_y) not in visited:
                if (next_x, next_y) != partner_pos:
                    new_path = path + [(next_x, next_y)]
                    visited.add((next_x, next_y))
                    queue.append(new_path)
    
    return None

def get_action_for_move(player_x, player_y, target_x, target_y, partner_pos):
    dx = abs(player_x - target_x)
    dy = abs(player_y - target_y)
    
    if max(dx, dy) <= 1:
        return f"USE {target_x} {target_y}"
    
    path = get_target_adjacent_position(player_x, player_y, target_x, target_y, partner_pos)
    
    if path and len(path) > 1:
        steps_to_move = min(4, len(path) - 1)
        next_x, next_y = path[steps_to_move]
        return f"MOVE {next_x} {next_y}"
    
    return "WAIT"

def get_path_length(start_x, start_y, target_x, target_y, partner_pos):
    path = get_target_adjacent_position(start_x, start_y, target_x, target_y, partner_pos)
    if path:
        return len(path) - 1
    return 999 

def determine_best_target_optimized(player_x, player_y, player_item, table_items, partner_pos):
    
    # 1. Priorité: Livrer si le plat est complet
    if "DISH-BLUEBERRIES-ICE_CREAM" in player_item:
        return EQUIPMENT_LOCATIONS['W']

    # 2. Priorité: Compléter le plat
    if "DISH" in player_item:
        item_list = player_item.split('-')
        
        missing_ingredients = [ing for ing in INGREDIENTS_NEEDED if ing not in item_list]
        
        if missing_ingredients:
            best_target_pos = None
            min_dist = 999
            
            # Évaluer les ingrédients manquants (B, I)
            for ingredient in missing_ingredients:
                target_pos = ITEM_LOCATIONS['B'] if ingredient == 'BLUEBERRIES' else EQUIPMENT_LOCATIONS['I']
                dist = get_path_length(player_x, player_y, target_pos[0], target_pos[1], partner_pos)
                
                if dist < min_dist:
                    min_dist = dist
                    best_target_pos = target_pos
                    
            if best_target_pos:
                return best_target_pos
    
    # 3. Priorité: Récupérer un plat semi-fini sur une table
    if player_item == "NONE":
        for pos, item in table_items:
            if "DISH-" in item and "DISH-BLUEBERRIES-ICE_CREAM" not in item:
                return pos
    
    # 4. Priorité: Commencer un nouveau plat (prendre DISH)
    if player_item == "NONE":
        return EQUIPMENT_LOCATIONS['D']
        
    # 5. Priorité: Déposer l'ingrédient sur une table libre pour optimiser les déplacements
    # Si le joueur porte un ingrédient seul (B ou I), mais que le DISH est loin, ou qu'il faut libérer la main
    if player_item in INGREDIENTS_NEEDED or ("DISH" in player_item and "BLUEBERRIES" in player_item and "ICE_CREAM" not in player_item and "DISH-BLUEBERRIES-ICE_CREAM" not in player_item):
        occupied_tables = [pos for pos, _ in table_items]
        
        for table_pos in ALL_TABLES:
            if table_pos not in occupied_tables:
                return table_pos
        
    return EQUIPMENT_LOCATIONS['W'] # Fallback: aller à la fenêtre

while True:
    try:
        turns_remaining = int(sys.stdin.readline())
    except:
        break

    inputs = sys.stdin.readline().split()
    player_x = int(inputs[0])
    player_y = int(inputs[1])
    player_item = inputs[2]
    
    inputs = sys.stdin.readline().split()
    partner_x = int(inputs[0])
    partner_y = int(inputs[1])
    partner_item = inputs[2]
    partner_pos = (partner_x, partner_y)
    
    num_tables_with_items = int(sys.stdin.readline())
    TABLE_ITEMS = []
    for _ in range(num_tables_with_items):
        inputs = sys.stdin.readline().split()
        table_x = int(inputs[0])
        table_y = int(inputs[1])
        item = inputs[2]
        TABLE_ITEMS.append(((table_x, table_y), item))
    
    try:
        sys.stdin.readline()
    except:
        pass
    
    num_customers = int(sys.stdin.readline())
    CURRENT_CUSTOMERS = []
    for _ in range(num_customers):
        inputs = sys.stdin.readline().split()
        customer_item = inputs[0]
        customer_award = int(inputs[1])
        CURRENT_CUSTOMERS.append((customer_item, customer_award))

    target_x, target_y = determine_best_target_optimized(player_x, player_y, player_item, TABLE_ITEMS, partner_pos)
    
    action = get_action_for_move(player_x, player_y, target_x, target_y, partner_pos)

    print(action)