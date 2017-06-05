print('整数を入力してください:')

try:
    input_num = int(input())
    print('入力値: ' + str(input()))
except ValueError:
    print('入力された値は整数ではありません。')
