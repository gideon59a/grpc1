import math


def square_root_factor(x, factor):
    print("square_root_factor has been called by the server")
    y = math.sqrt(x) * factor
    return y


def mult(x1, x2):
    print("mult has been called by the server")
    y = x1 * x2
    return y


if __name__ == "__main__":
    print(square_root_factor(121, 10))
    print(mult(2, 3))

