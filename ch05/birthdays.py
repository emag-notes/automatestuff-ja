birthdays = {'アリス': '4/1', 'ボブ': '12/12', 'キャロル': '4/4'}

while True:
    print('名前を入力してください:(終了するには Enter だけ押してください)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(name + ' の誕生日は ' + birthdays[name] + ' です。')
    else:
        print(name + ' の誕生日は未登録です。')
        print('誕生日を入力してください:')
        birthday = input()
        birthdays[name] = birthday
        print('誕生日データベースを更新しました。')