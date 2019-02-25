import ctypes

spam = ctypes.CDLL('./libspam.so')
spam.sum.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)


def our_function(numbers):
    global spam
    num_numbers = len(numbers)
    array_type = ctypes.c_int * num_numbers
    result = spam.sum(array_type(*numbers), ctypes.c_int(num_numbers))
    return int(result)


if __name__ == '__main__':
    print("Llamando a función sum de spam")
    nums = [1, 2, 3, 4, 5]
    print("Sumando {} ===> {}".format(nums, our_function(nums)))
