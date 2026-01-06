nums = [12, 5, 8, 3, 10, 7]
print("Largest:", max(nums))
print("Smallest:", min(nums))
nums.sort()
print("Sorted list:", nums)
nums.append(15)
print("After adding new number:", nums)
nums = [x for x in nums if x % 2 != 0]
print("After removing even numbers:", nums)
