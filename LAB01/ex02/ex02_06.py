x, y = input("Nhập X, Y:").split()
multilist = [[i * j for i in range(int(y))] for j in range(int(x))]
print(multilist)