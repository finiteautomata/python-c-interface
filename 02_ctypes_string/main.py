import ctypes

lib = ctypes.CDLL('./libstringtools.so')

lib.strconcat.argtypes = (ctypes.c_char_p, ctypes.c_char_p)


def concat_strings(str1, str2):
    b1 = str1.encode('utf-8')
    b2 = str2.encode('utf-8')

    lib.strconcat.restype = ctypes.c_char_p

    return lib.strconcat(b1, b2)


if __name__ == '__main__':
    print("Llamando a función strconcat de libstrtools")
    print(concat_strings("Hola", " mundo"))
