def digital_root(n):
    while len(str(n)) != 1:
        n = sum_arr(n)
    return n

def sum_arr(string):
    array = [int(i) for i in str(string)]
    sum_array = sum(array)
    return sum_array

print(digital_root(12312323333))