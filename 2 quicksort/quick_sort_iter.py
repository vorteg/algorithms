def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_iterative(arr):
    size = len(arr)
    stack = [(0, size - 1)]
    print("stack: ",stack)

    while stack:
        low, high = stack.pop()

        if low < high:
            pi = partition(arr, low, high)

            if pi - low < high - pi:
                stack.append((low, pi - 1))
                stack.append((pi + 1, high))
            else:
                stack.append((pi + 1, high))
                stack.append((low, pi - 1))

# Ejemplo de uso
lista = ["John",
    "Emily",
    "Michael",
    "Sarah",
    "David"]

if __name__ == "__main__":
    print("Lista original:", lista)
    quicksort_iterative(lista)
    print("Lista ordenada:", lista)