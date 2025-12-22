num = int(input("Enter a number: "))
num_1 = 1
num_2 = 1
while 0 < num_1 <= num:
    num_2 = num_2 * num_1
    num_1 = num_1 + 1
if num > -1:
    print(num_2)
else:
    print("Please write number between 0 and +infinity"-1)