from give_bmi import apply_limit, give_bmi

res = give_bmi([2.71, 1.15], [165.3, 38.4])

print(type(res))
for i in res:
    print(i)

print(apply_limit(res, 26))
