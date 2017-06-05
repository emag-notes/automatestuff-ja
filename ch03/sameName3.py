def spam():
    global eggs
    eggs = 'spam'


def bacon():
    egs = 'bacon'


def ham():
    print(eggs)


eggs = 42
ham()
spam()
ham()
print(eggs)
