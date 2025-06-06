"""
练习: while循环

描述：
在数字列表中查找第一个偶数。

请补全下面的函数，使用while循环在数字列表中查找并返回第一个偶数。
如果列表中没有偶数，则返回None。
"""

def find_first_even(numbers):
    """
    在数字列表中查找第一个偶数
    
    参数:
    - numbers: 整数列表
    
    返回:
    - 列表中的第一个偶数，如果没有偶数则返回None
    """
    # 请在下方编写代码
    i = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            return numbers[i]
        i += 1
    return None

def sum_numbers_while(n):
    """
    使用 while 循环从 1 加到 n
    
    参数:
    - n: 正整数
    
    返回:
    - 从 1 加到 n 的总和
    """
    i = 1
    total = 0
    while i <= n:
        total += i
        i += 1
    return total