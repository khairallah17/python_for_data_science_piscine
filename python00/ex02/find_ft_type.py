def all_thing_is_obj(object: any) -> int:

    types = {
        list: "List",
        dict: "Dict",
        tuple: "Tuple",
        set: "Set"
    }

    x = types.get(type(object))

    if type(object) == str :
        print(f"{object} is in the kitchen : {type(object)}")
    elif x is not None :
        print(f"{x} : {type(object)}")
    else :
        print("Type Not found")

    return 42
