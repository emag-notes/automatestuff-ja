my_pets = ['Zophie', 'Pooka', 'Fat-tail']

print('ペットの名前を入力してください:')
name = input()
if name in my_pets:
    print(name + ' は私のペットです。')
else:
    print(name + ' という名前のペットは飼っていません。')
