print('名前を入力してください。')
name = input()

print('年齢を入力してください。')
age = int(input())

if name == 'Alice':
    print('やあ、Alice。')
elif age < 12:
    print('Aliceじゃないね、お嬢ちゃん')
elif age > 2000:
    print('Aliceはお前のような不死身ではない、吸血鬼め。')
elif age > 100:
    print('Aliceじゃないね、お婆ちゃん。')