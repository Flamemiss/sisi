def sum_to_n(n):
    """计算1到n的和"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# 测试
n = int(input("请输入N: "))
result = sum_to_n(n)
print(f"1到{n}的和是: {result}")
