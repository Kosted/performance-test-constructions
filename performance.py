import random
import time




def great(a):
    if a[1] > global_int:
        return a


def timer(funk, primal_arr, about ):
    final_time = 0
    arr = primal_arr[:]

    for i in range(number_of_tests):
        current_time = time.time()
        l = funk(arr)

        final_time += time.time() - current_time
        # print(l)
    print(about, final_time)


def test_for(arr):
    l = list()
    for i in arr:
        if i[1] > global_int:
            l.append(i)
    return l


def test_map(arr):
    l = list(map(great, arr))

    return l


def test_generator(arr):
    l = [x for x in arr if x[1] > global_int]
    return l


def test_remove(arr):

    for i in arr:
        if i[1] > global_int:
            arr.remove(i)
    return arr


def test_pop(arr):
    # reverse_list = arr[::]
    for i, e in reversed(list(enumerate(arr))):

        if e[1] > global_int:
            arr.pop(i)
    return arr


def test_pop_while(arr):
    i = len(arr)-1
    while i > -1:
        if arr[i][1] > global_int:
            arr.pop(i)
        i -= 1
    return arr

# отбираются числа меньше данного
global_int = 500

# количество кортежей в массиве
arr_size = 100

# сколько раз проганяется функция
number_of_tests = 1000

if __name__ == "__main__":

    arr = [(x, random.randint(-1, 1000)) for x in range(arr_size)]

    print("elem count = ", arr_size, ';\nnumber of tests = ', number_of_tests, "\nnumbers that are greater than: ", global_int, "\n")

    timer(test_for, arr,       "for      ")
    timer(test_map, arr,       "map      ")
    timer(test_generator, arr, "generator")
    timer(test_remove, arr,    "remove   ")
    timer(test_pop, arr,       "pop      ")
    timer(test_pop_while, arr, "pop while")




