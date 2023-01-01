#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
<<<<<<< HEAD
        ret = fct(*args)
        return ret
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
=======
        return fct(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
>>>>>>> b55092ece4330ce78c9ad7033407fc5ad8465e5d
        return None
