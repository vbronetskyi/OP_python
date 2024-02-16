"""My ex"""
class MyException(Exception):
    pass

def myexcept_raise_func():
    raise MyException("My Exception")

def except_func():
    try:
        myexcept_raise_func()
    except MyException as e:
        print("My Exception handled:", e)
    except (KeyError, IndexError) as e:
        print("Other exception handled:", e)
    except Exception as e:
        print("Exception not handled:", e)

except_func()