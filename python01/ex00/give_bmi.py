def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:

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

    try:

        res = [b > limit for b in bmi]
        return res

    except Exception:
        print("error!")
        raise
