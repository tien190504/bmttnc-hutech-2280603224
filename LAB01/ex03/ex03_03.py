def create_tuple_from_list(lst):
    return tuple(lst)

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ").split(",")
numbers = list(map(int, input_list))
my_tuple = create_tuple_from_list(numbers)
print("LIST: ", numbers)
print("TUPLE: ", my_tuple)