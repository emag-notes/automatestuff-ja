def collatz(input_num):
    print(input_num)

    if input_num == 1:
        return 1

    if input_num % 2 == 0:
        collatz(input_num // 2)
    elif input_num % 2 == 1:
        collatz(3 * input_num + 1)


print('整数を入力してください:')
input_num = int(input())
collatz(input_num)
