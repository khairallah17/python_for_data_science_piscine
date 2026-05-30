def slice_me(family: list, start: int, end: int) -> list:
    """
    generates a slices version of the list depending on the start and end.

    Args:
        family (list): the array to slice.
        start (int): start index.
        end (int): number of entries.

    Returns:
        list: a new list for the sliced version of the parameters list.
    """
    try:
        print(f"my shape is ({len(family)},{len(family[0])})")
        new_res = family[start:end]
        return new_res
    except Exception:
        print("error!")
        return None
