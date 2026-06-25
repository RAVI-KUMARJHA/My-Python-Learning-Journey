# ---------------------------:Returns the index of elements whose sum is targeted number:-----------------------------------------

lis = [3, 3]
target = 6


def twoSum(nums, target):

    new = []

    for i in range(len(lis)):
        for j in range(len(lis)):
            if (i) == (j):
                continue
            elif lis[i] + lis[j] == target:
                new.append(i)
                new.append(j)

    return list(set(new))


print(twoSum(lis, target))
