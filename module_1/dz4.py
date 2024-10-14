n = int(input())
numbers = input()
numbers = numbers.split(" ")
arr = []
for i in range(n):
    arr.append(int(numbers[i]))
number_to_delete = int(input())
counter = 0
for i in range(n):
    if arr[i] != number_to_delete:
        print(arr[i], end=" ")
