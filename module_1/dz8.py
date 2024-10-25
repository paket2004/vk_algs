n = int(input())
arr = input()
arr = arr.split(" ")
my_stack = []
for i in range(n):
    arr[i] = int(arr[i])
for i in arr:
    if i % 2 == 0:
        my_stack.append(i)
print(my_stack[-1])
