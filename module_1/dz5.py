n = int(input())
arr = input()
arr = arr.split(" ")
maximum = int(arr[0])
for i in range(n):
    if int(arr[i]) > maximum:
        maximum = int(arr[i])
print(maximum)
