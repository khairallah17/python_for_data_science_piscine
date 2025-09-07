import sys

try :

    if len(sys.argv) > 2 :
        raise AssertionError("more than one argument is provided")
    if type(sys.argv[1]) is str :
        raise AssertionError("argument is not an integer")

    


except AssertionError as error :
    print(error)
