def NULL_not_found(object: any) -> int:
    
    types = {
        "None": "Nothing",
        "nan": "Cheese",
        "0": "Zero",
        "": "Empty",
        "False" : "Fake"
    }

    x = types.get(str(object), None)

    if x is None :
        print("Type not Found")
        return 1

    print(f"{x}: {object} {type(object)}")

    return 42
