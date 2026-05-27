def slice_me(family: list, start: int, end: int) -> list:

    try:
        print(f"my shape is ({len(family)},{len(family[0])})")
        new_res = family[start:end]
        print(f"my new shape is ({len(new_res)},{len(new_res[0])})")
        return new_res
    except Exception:
        print("error!")
