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
search(aList, 20)
