
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


# Хорошо! Есть еще вариант с быстрой сортировкой
# Быстрая сортировка
def quicksort(arr):
    if len(arr) < 2:
        # базовый случай, массив с 0 или 1 элементом уже отсортирован
        return arr
    else:
        # рекурсивный случай. выберем опорный элемент pivot
        pivot = arr[0]
        # подмассив всех элементов, меньших, чем опорный элемент pivot
        less = [i for i in arr[1:] if i <= pivot]
        # подмассив всех элементов, превышающих опорный элемент pivot
        greater = [i for i in arr[1:] if i > pivot]
        # обединяем в порядке "сортировка для меньшего подмассива – опорный элемент – сортировка для большего подмассив"
        return quicksort(less) + [pivot] + quicksort(greater)

# Максимум - это последний элемент отсортированного списка
def maximum(arr):
    return quicksort(arr)[-1]

 # Минимум - это первый элемент отсортированного списка
def minimum(arr):
    return quicksort(arr)[0]
print('\nБыстрая сортировка')
print('min =', minimum([4,6,2,1,9,63,-134,566]))
print('max =', maximum([4,6,2,1,9,63,-134,566]))
