import ctypes

spam = ctypes.CDLL('./libspam.so')
spam.sum.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_int))

def our_function(numbers):
    global spam
    num_numbers = len(numbers)
    array_type = ctypes.c_int * num_numbers
    result = spam.sum(ctypes.c_int(num_numbers), array_type(*numbers))
    return int(result)
