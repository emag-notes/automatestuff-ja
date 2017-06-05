all_guests = {
    'アリス': {
        'リンゴ': 5, 'プレッツェル': 12
    },
    'ボブ': {
        'ハムサンド': 3, 'リンゴ': 2
    },
    'キャロル': {
        'コップ': 3, 'アップルパイ': 1
    }
}


def total_brought(guests, item):
    num_brought = 0
    for v in guests.values():
        num_brought = num_brought + v.get(item, 0)
    return num_brought


def print_total_brought(item):
    print(' - '  + item + ' ' + str(total_brought(all_guests, item)))


print('持ち物の数:')
print_total_brought('リンゴ')
print_total_brought('コップ')
print_total_brought('ケーキ')
print_total_brought('ハムサンド')
print_total_brought('アップルパイ')