def sum_even(numbers):
    total = 0
    for i in numbers:
        if i % 2 == 0:
            total += i
    return total
input_list = input("Enter a list of numbers: ").split(',')
input_list = list(map(int, input_list))
print(sum_even(input_list))