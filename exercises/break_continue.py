"""
练习: break和continue语句

描述：
返回从1到n的所有非3的倍数的整数列表。

请补全下面的函数，使用continue语句跳过3的倍数。
"""

def skip_multiples_of_three(n):
    result = []
    for i in range(1, n+1):
        if i % 3 == 0:
            continue
        result.append(i)
    return result

    # return [i for i in range(n+1) if i % 3 != 0]
