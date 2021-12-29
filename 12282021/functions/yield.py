# this is for the squares ;3

def nextSquare():
    i = 1

    while True:
        yield i*i
        i += 1

for num in nextSquare():
    if num > 100:
        break
    print(num)
