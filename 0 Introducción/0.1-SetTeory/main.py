"""
FelipedelosH
2025

set
"""
_empty = {}
print(f"EMPTY SET: {_empty}")
_vowels = {'a', 'e', 'i', 'o', 'u'}
print(f"Vowles SET: {_vowels}")
_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(f"Numbers SET: {_numbers}")
_even_numbers = {2,4,6,8,0}
print(f"Even numbers SET: {_even_numbers}")
_other = {0, '1', 7, 'u'}
print(f"Other SET: {_other}")

_vowels_union_numbers = _vowels | _numbers
print(f"Vowles UNION NUMBERS: {_vowels_union_numbers}")

_numbers_intersection_other = _numbers & _other
print(f"Number INTERSECTION Other: {_numbers_intersection_other}")

_vowels_subtraction_other = _vowels - _other
print(f"Vowels SUBTRACTION Other: {_vowels_subtraction_other}")

_even_is_contained_in_numbers = _even_numbers.issubset(_numbers)
print(f"Even is contained in numbers? RTA: {_even_is_contained_in_numbers}")

def generatePowerSet(a):
    elementos = list(a)
    return _generatePowerSet(elementos)

def _generatePowerSet(elementos):
    if not elementos:
        return [set()]
    
    primero = elementos[0]
    resto_power_set = _generatePowerSet(elementos[1:])
    
    resultado = []
    for subconjunto in resto_power_set:
        resultado.append(subconjunto)
        resultado.append(subconjunto.union({primero}))
    
    return resultado

_power_set = generatePowerSet({'a', 'b', 'c'})
print("Power set of {a, b}: " + f"{_power_set}")

set_a = {'a'}
print(f"Complement of SET A: {_vowels - set_a}")