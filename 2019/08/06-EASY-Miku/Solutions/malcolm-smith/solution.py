def mikuPrint(n):
    for i in range(n + 1):
        if i % 9 == 0:
            print('Miku')
        elif i % 3 == 0:
            print('Mi')
        else:
            print(i)

mikuPrint(18)