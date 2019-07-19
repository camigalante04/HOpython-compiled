import ctypes as C
math = C.CDLL('./libmymath.so')
math.add_float.restype = C.c_float
math.add_float.argtypes = [C.c_float, C.c_float]
math.add_float(3,4)

math.add_int.restype = C.c_int
math.add_int.argtypes = [C.c_int, C.c_int]
math.add_int(2,6)

math.add_float_ref.restype = C.c_float
math.add_float_ref.argtypes = [C.c_float, C.c_float]
math.add_ref
