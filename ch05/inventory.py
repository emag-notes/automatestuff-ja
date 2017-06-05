inventory = {'ロープ': 1, 'たいまつ': 6, '金貨': 42, '手裏剣': 1, '矢': 12}
dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']


def display_inventory(inventory):
    print('持ち物リスト:')

    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total = item_total + v

    print("アイテム総数: " + str(item_total))


def add_to_inventory(inventory, added_items):
    new_inventory = inventory.copy()

    for item in added_items:
        new_inventory[item] = new_inventory.get(item, 0) + 1

    return new_inventory

print('[初期状態]')
display_inventory(inventory)

print('-------------------------')
print('[ドラゴン征伐後]')
new_inventory = add_to_inventory(inventory, dragon_loot)
display_inventory(new_inventory)
