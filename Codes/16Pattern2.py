# wap print this pattern 1 3 7 11 13 15 using for loop

for i in range(1,16,2):
    if i==9 or i==5:
        continue        # continue skip current iteration
    else:
        print(i)