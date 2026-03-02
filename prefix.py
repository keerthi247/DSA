# Prefix Sum Example

arr = [2, 4, 6, 8]

prefix = [0] * len(arr)

prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

print("Prefix array:", prefix)

# Example: sum from index 1 to 3
L = 1
R = 3

if L == 0:
    result = prefix[R]
else:
    result = prefix[R] - prefix[L-1]

print("Sum from index", L, "to", R, "=", result)
