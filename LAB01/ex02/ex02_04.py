list = [i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]
print(','.join(str(i) for i in list))
