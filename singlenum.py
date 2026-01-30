def SingleNumberOptimal(num):
    result = 0
    for i in range(len(num)):
        result ^= num[i]
    return result

num = [1, 2, 1, 2, 4]
print(SingleNumberOptimal(num))

num = [1, 1, 2]
print(SingleNumberOptimal(num))

num = [1]
print(SingleNumberOptimal(num))