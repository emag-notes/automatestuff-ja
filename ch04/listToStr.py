def listToStr(list):
    str = ''
    for i in range(0, len(list)):
        if i != len(list) - 1:
            str = str + list[i] + ', '
        else:
            str = str + 'and ' + list[i]
    return str


print(listToStr(['apples', 'bananas', 'tofu', 'cats']))
