from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  #Function implementing merging of two sorted arrays
  #Input: nums1 -> array
  #       m -> number of elements of nums1
  #       nums2 -> array
  #       n -> number of elements of nums2
  l1 = nums1[:]
  l2 = nums2[:]
  curr, i, j = 0, 0, 0
  while i < m and j < n:
    if l1[i] < l2[j]:
      nums1[curr] = l1[i]
      i += 1
    else:
      nums1[curr] = l2[j]
      j += 1
    curr += 1
  while i < m:
    nums1[curr] = l1[i]
    curr += 1
    i += 1
  while j < n:
    nums1[curr] = l2[j]
    curr += 1
    j += 1


# Do noT change the following code
nums1 = []
nums2 = []
for item in input().split(', '):
  nums1.append(int(item))
for item in input().split(', '):
  nums2.append(int(item))
m = int(input())
n = int(input())
merge(nums1, m, nums2, n)
print(nums1)
