def give_bmi(height: list[int | float], weight: list[int | float]) \
            -> list[int | float]:
    """
    calculate the BMI for a given list of heights and weights.

    Args:
        height (list[int | float]): the heights.
        weight (list[int | float]): the weights.

    Returns:
        list[int | float]: the results of each entry for the lists
        for the following formula (weight/(height)**2).
    """
    try:
        res = []

        if len(height) != len(weight):
            raise Exception("height and weight are not the same length")

        max_size = len(height)

        for i in range(0, max_size):
            res.append(weight[i] / (height[i] ** 2))

        return res

    except Exception:
        print("error!")
        raise


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    check if the lists of BMIs are heigher or lower than the limit.

    Args:
        bmi (list[int | float]): BMIs list.
        limit (int): limit.

    Returns:
        list[bool]: for each entry of the list we insert True or False
        if either the entry is lower or higher than the limit.
    """
    try:

        res = [b > limit for b in bmi]
        return res

    except Exception:
        print("error!")
        raise
