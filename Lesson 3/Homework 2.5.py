a = int(input("Write number:"))
b = int(input("Write number:"))
c = 0
d = 0
while a <= b:
    while c < a:
        c = c + 1
        if a % c == 0:
            d = d+1
    if c == a and d == 1 or d == 2:
        print(a)
        a = a + 1
        c = 0
        d = 0
    else:
        a = a + 1
        c = 0
        d = 0


