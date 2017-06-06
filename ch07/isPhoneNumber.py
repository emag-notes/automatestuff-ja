def is_phone_number(text):
    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True


print('415-555-4242 は電話番号:')
print(is_phone_number('415-555-4242'))

print('Moshi moshi は電話番号:')
print(is_phone_number('Moshi moshi'))

print()

message = '明日 415-555-1011 に電話してください。オフィスは 415-555-9999 です。'
for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print('電話番号が見つかりました: ' + chunk)
print('完了')