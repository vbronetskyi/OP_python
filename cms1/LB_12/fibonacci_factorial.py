"""Lab_12.2"""
import time

def factorial_recursive(numb: int) -> int:
    """
    returns the factorial of numb (recurs)
    >>> factorial_recursive(10)
    3628800
    >>> factorial_recursive(3)
    6
    """
    if numb == 1 :
        return numb
    else : return numb * factorial_recursive(numb - 1)
#print(factorial_recursive(10))

def factorial_iterative(numb: int) -> int:
    """
    returns the factorial of numb (without recurs)
    >>> factorial_recursive(10)
    3628800
    >>> factorial_recursive(3)
    6
    """
    solut = 1
    for j in range(numb) : solut *= (j+1)
    return solut

def fibonacci_recursive(numb: int) -> int:
    """
    returns the nth number from the Fibonacci sequence (With recurs)
    >>> fibonacci_recursive(4)
    5
    >>> fibonacci_recursive(18)
    4181
    """
    if numb == 0:
        return 1
    elif numb == 1:
        return numb
    else : return fibonacci_recursive(numb - 1) + fibonacci_recursive(numb - 2)
#print(fibonacci_recursive(4))

def fibonacci_iterative(numb: int):
    """
    returns the nth number from the Fibonacci sequence (without recurs)
    >>> fibonacci_recursive(4)
    5
    >>> fibonacci_recursive(18)
    4181
    """
    numb -=1
    solut = [1,1]
    for i in numb:
        solut.append(solut[i+1]+solut[i])
    return solut[-1]

def numbers_time_test(function=0, realisation=0, verbose=False):
    """
    This function will return the time spent
    on the execution of the function
    """
    start_time = time.time()
    if function == 0:
        if realisation==0:
            end_time=factorial_recursive(25)
            if verbose:
                solut = (f'Function result is: {factorial_recursive(25)} \
                    Time taken: end_time - start_time')
                print(solut)
            elif verbose
    
