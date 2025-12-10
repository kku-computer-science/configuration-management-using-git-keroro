def quick_sort(arr):
    print("quick sort")
    result = arr
    return arr

def bubble_sort(arr):
    print("bubble sort")
    result = arr.copy()
    n = len(result)

    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result



if __name__ == "__main__":
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
