first = 520
print(first)

def change():
    global first
    second = '530'
    first = second

change()
print(first)