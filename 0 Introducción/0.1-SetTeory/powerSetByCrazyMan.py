"""
FelipedelosH
2025


Generate a power set in base a Numeric SYSTEM
"""
def generateElementsEnumeration(set):
    _order = []

    for i in set:
        _order.append(i)

    return _order


def generateCombinatory(arr, n):
    result = []
    
    def backtrack(start, current):
        if len(current) == n:
            result.append(current.copy())
            return
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result


def generatePowerSet(_set):
    PA = [set()]
    return _generatePowerSet(len(_set), PA, generateElementsEnumeration(_set))


def _generatePowerSet(iterator, PA, enum):
    if iterator == 0:
        return PA

    for i in generateCombinatory(enum, iterator):
        PA.append(set(i))

    iterator = iterator - 1
    return _generatePowerSet(iterator, PA, enum)


_set = {'a', 'b'}
print(f"Power SET of {_set}:")
print(generatePowerSet(_set))
