# Insertion sort is much more efficient than Bubble and Selection sort.

def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = temp


if __name__ == '__main__':
    arr = [6, 4, 89, 23, 9, 1, 22, 3]

    insertionSort(arr)

    print(arr)
    print(*arr)