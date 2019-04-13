from linkedlist import MatthewLL


def verifyListsAreEqual(newListImplementation, regularList):
    for i in range(len(regularList)):
        assert newListImplementation.index(i) == regularList[i]


def setupLists():
    ll = MatthewLL()
    ll.add(4)
    ll.add(7)
    ll.add(3)
    ll.add(2)

    regularList = [4, 7, 3, 2]

    return ll, regularList


def addTests():
    testList, regularList = setupLists()
    verifyListsAreEqual(testList, regularList)


def popTests():
    testList, regularList = setupLists()

    testList.pop(3)
    regularList.pop(3)
    verifyListsAreEqual(testList, regularList)

    testList.pop(0)
    regularList.pop(0)
    verifyListsAreEqual(testList, regularList)


addTests()
popTests()


