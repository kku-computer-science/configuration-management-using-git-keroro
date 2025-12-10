def quick_sort(arr):
    print("quick sort")
    result = arr
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


user_input = input("enter number(example: 5 6 4): ")
data = list(map(int, user_input.split()))

print("sort:")
print("1 = Bubble Sort")
print("2 = Quick Sort")
choice = input("enter number (1 or 2): ")

if choice == "1":
    result = bubble_sort(data)
    print("Bubble Sort result:", result)
elif choice == "2":
    result = quick_sort(data)
    print("Quick Sort result:", result)
else:
    print("please enter 1 or 2")
