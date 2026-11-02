import random


def generate(n, lo, hi):
    return [random.randint(lo, hi) for _ in range(n)]


def show(a):
    print("{" + ",".join(f"[cell - {i},value - {v}]" for i, v in enumerate(a)) + "}")


def bubble_sort(a, asc=True):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if asc == True:
    if a[j] > a[j + 1]:
        a[j], a[j + 1] = a[j + 1], a[j]
else:
    if a[j] < a[j + 1]:
        a[j], a[j + 1] = a[j + 1], a[j]  # обмін сусідніх
    return a


def insertion_sort(a, asc=True):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        if asc == True:
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]
                j -= 1
        else:
            while j >= 0 and a[j] < key:
                a[j + 1] = a[j]
                j -= 1
        a[j + 1] = key
    return a
    

def selection_sort(a, asc=True):
    for i in range(len(a) - 1):
        m = i
        for j in range(i + 1, len(a)):
            if asc == True:
                if a[j] < a[m]:
                    m = j
            else:
                if a[j] > a[m]:
                    m = j
        a[i], a[m] = a[m], a[i]
    return a


if __name__ == "__main__":
    arr = generate(10, -20, 50)
    print("Початковий масив:")
    show(arr)

    for sort in (bubble_sort, insertion_sort, selection_sort):
        print(f"\n{sort.__name__}:")
        print("  за зростанням:")
        show(sort(arr.copy(), True))
        print("  за спаданням:")
        show(sort(arr.copy(), False))
