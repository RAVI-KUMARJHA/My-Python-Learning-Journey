"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n))."""

# ----------------------------:Question number 4 :----------------------------------

nums1 = [1, 2]
nums2 = [3, 4]
# Output: 2.50000

new = []
for i in nums1:
    new.append(i)


for j in nums2:
    new.append(j)


new.sort()
print(new)

if len(new) % 2 == 0:

    mid = int(len(new) / 2)

    median = new[mid] + new[mid - 1]
    y = median / 2
#     print(new[mid])
#     print(new[mid - 1])
    p = f"{y:.5f}"
    print(y)


else:

    odd = new[int(len(new) / 2)] / 2
    print(odd)

# print(med)
