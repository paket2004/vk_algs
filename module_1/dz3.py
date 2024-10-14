n = int(input())
numbers = input()
numbers = numbers.split(" ")
arr = []
for i in range(n):
    arr.append(int(numbers[i]))
arr_2 = []
counter = 0
for i in range(n):
    if arr[i] != 0:
        arr_2.append(arr[i])
    else:
        counter += 1
print(arr_2 + [0] * counter)
