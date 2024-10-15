n = int(input())
arr = input()
arr = arr.split(" ")

for i in range(n):
    arr[i] = int(arr[i])

min_diff = [arr[0], arr[1], abs(arr[1] - arr[0])]

for i in range(2, n):
    if abs(arr[i] - arr[i - 1]) < min_diff[2]:
        min_diff[2] = abs(arr[i] - arr[i - 1])
        min_diff[0] = arr[i - 1]
        min_diff[1] = arr[i]
for i in range(len(min_diff)):
    if i < 2:
        print(min_diff[i], end=" ")

    
