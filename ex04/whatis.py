import sys

try :

    if len(sys.argv) != 2:
        if len(sys.argv) > 2 :
            raise AssertionError("more than one argument is provided")
   
    number = int(sys.argv[1])

    if number & 1:
        print("I'm Odd.")
    else :
        print("I'm Even.")



except Exception as error :
    if type(error) is ValueError :
        print("AssertionError: argument is not an integer")
    elif type(error) is AssertionError :
        print(f"AssertionError: {error}")
