
def coolShape(size):
    for i in range(size):
        print("*" * (i + 1))
    for i in range(size):
        print(" " * (size - (i + 1)) + "*" * (i + 1))

coolShape(11)