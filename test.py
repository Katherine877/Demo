# 鸡兔同笼
def chicken_rabbit(heads, legs):
    for i in range(heads + 1):
        j = heads - i
        if 2 * i + 4 * j == legs:
            return i, j
    return None, None

heads = 35
legs = 94
chicken, rabbit = chicken_rabbit(heads, legs)
if chicken is not None:
    print('鸡有%d只，兔有%d只' % (chicken, rabbit))
else:
    print('无解')
