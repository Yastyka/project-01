
my_list = [3, 8, 16, 21, 32, -17, 673]

def minimum(my_list):
    min_value = my_list[0]
    for i in range(len(my_list)):
        if min_value > my_list[i]:
            min_value = my_list[i]
    return (min_value)

print(minimum([3, 8, 16, 21, 32, -17, 673]))

my_list = [3, 8, 16, 21, 32, -17, 673]
   
def maximum(my_list):
    max_value = my_list[0]
    for i in range(len(my_list)):
        if max_value < my_list[i]:
            max_value = my_list[i]
    return (max_value)

print(maximum([3, 8, 16, 21, 32, -17, 673]))


