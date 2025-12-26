a = int(input("Write number:"))
b = int(input("Write number:"))
c = 0
if a == b:
    print(a)
while a > b:
    c = c + b
    b = b + 1
    if b == a:
        c = c + b
        break
while a < b:
    c = c + a
    a = a + 1
    if a == b:
        c = c + a
        print(c)
        break






