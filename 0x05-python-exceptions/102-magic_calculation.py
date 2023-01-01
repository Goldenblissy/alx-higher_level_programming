#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
<<<<<<< HEAD
                result += (a ** b) / i
        except Exception:
            result = b + a
            break
    return (result)
=======
                result += a**b / i
        except Exception:
            result = a + b
            break
    return result
>>>>>>> b55092ece4330ce78c9ad7033407fc5ad8465e5d
