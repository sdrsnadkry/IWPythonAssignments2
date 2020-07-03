def binary_search(lists, item):
    first = 0
    last = len(lists)-1
    found = -1

    while(first <= last and found == -1):
        mid = (first+last)//2

        if lists[mid] == item:
            found = lists.index(item)
        else:
            if item < lists[mid]:
                last = mid-1
            else:
                first = mid+1

    return found


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 5))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 9))
