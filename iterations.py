count = 0
while count < 10:
    print(count)
    count += 1

'''
0
1
2
3
4
5
6
7
8
9
'''

count_ext = 0
count_int = 0

while count_ext < 5:
    while count_int < 6:
        print(count_ext, count_int)
        count_int += 1
        if count_int >= 3:
            break

    count_ext += 1
    count_int = 0

