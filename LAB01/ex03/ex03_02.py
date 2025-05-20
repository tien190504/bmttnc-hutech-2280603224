def dao_nguoc_list(lst):
    return lst[::-1]
input_list = input("Nhập list: ").split(",")
numbers = list(map(int, input_list))
print(dao_nguoc_list(numbers))