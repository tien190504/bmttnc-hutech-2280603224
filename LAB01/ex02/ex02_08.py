def diveces_by_5(binary_number):
    decimal = int(binary_number, 2)
    if decimal % 5 == 0:
        return True
    return False

list = input("Nhập chuỗi số nhị phân: ")
list = list.split(',')

list_into_5 = [number for number in list if diveces_by_5(number)]

output = f"Các số nhị phân chi hết cho 5 là: {','.join(list_into_5)}" if len(list_into_5) > 0 else 'Không có số nhị phân chi hết cho 5'

print(output)