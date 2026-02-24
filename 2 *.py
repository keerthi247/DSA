def two_pointer_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]

        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1

    return False

# Example
arr = [1, 2, 3, 4, 6, 8]   # Sorted array
target = 10

if two_pointer_sum(arr, target):
    print("Pair found")
else:
    print("Pair not found")
