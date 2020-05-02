def mergesort(lst):
    if len(lst) < 2:
        return lst
    mid = len(lst) // 2
    L = lst[:mid]
    R = lst[mid:]

    mergesort(L)  # Sorting the first half
    mergesort(R)  # Sorting the second half

    i = j = k = 0

    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(L):
        lst[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        lst[k] = R[j]
        j += 1
        k += 1
    return lst


print(mergesort([6, 5, 4, 3, 2]))
