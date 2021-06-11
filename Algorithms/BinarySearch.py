def search(searchList, key):
    mid = int(len(searchList) / 2)
    print("Find center point ", str(searchList[mid]))
    if mid == 0:
        print("Key not found")
        return key
    elif key == searchList[mid]:
        print("Key found")
        return searchList[mid]
    elif key > searchList[mid]:
        print("searchList contains ", searchList[mid:len(searchList)])
        search(searchList[mid:len(searchList)], key)
    else:
        print("searchList contains ", searchList[0:mid])
        search(searchList[0:mid], key)


aList = list(range(1, 21))
print(aList)
print("----------")
search(aList, 17)
print("-------------------")


def binary_iterative(elements, search_item):

    left, right = 0, len(elements) - 1

    while left <= right:

        middle_dex = (left + right) // 2
        middle_el = elements[middle_dex]

        if middle_el == search_item:
            return middle_dex
        elif middle_el < search_item:
            left = middle_dex + 1
        elif middle_el > search_item:
            right = middle_dex - 1
    
    return None

aList = list(range(0, 21))
print(aList)
print("----------")
print(binary_iterative(aList, 17))