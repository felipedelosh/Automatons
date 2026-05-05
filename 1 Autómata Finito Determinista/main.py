"""
FelipedelosH
2026

Automaton Examples
"""
from AFD import Automaton

# ======================================
# Example 01: contains char 'a'
# ======================================
_states = ["q0", "q1"]
_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","á", "é", "í", "ó", "ú"]
_transitions = [
    ("q0", "q0", i) for i in _alphabet if i != "a"
]
_transitions = _transitions + [
    ("q0", "q1", "a")
]
_transitions = _transitions + [
    ("q1", "q1", i) for i in _alphabet
]

_q0 = "q0"
_F = ["q1"]
a = Automaton(_states, _alphabet, _transitions, _q0, _F)

print("="*20)
print(f"El Autómata 01: que determina si una palabra contiene el caracter 'a'")
print(f"Tamaño del alfabeto: {len(a.alphabet)}")
print(a.alphabet)
print(f"Cantidad de nodos: {len(a.states)}")
print(a.states)
print(f"Cantidad de transiciones: {len(a.transitions)}")
print(a.transitions)
print(f"El autómata es completo? >> {a.isComplete()}")
print(f"El autómata es determinista? >> {a.isDeterministic()}")
print(f"Pruebas:")
_test = ["andres", "homero", "juana", "kevin"]
for i in _test:
    print(f"Prueba: {i} >> {a.process(i)}")


# ======================================
# Example 02: Only binary numbers that are multiples of 2
# ======================================
print("="*20)
_states = ["q0", "q1"]
_alphabet = ["0", "1"]
_transitions = [
    ("q0", "q0", "1")
]

_transitions = _transitions + [
    ("q0", "q1", "0")
]

_transitions = _transitions + [
    ("q1", "q0", "1")
]

_transitions = _transitions + [
    ("q1", "q1", "0")
]

_q0 = "q0"
_F = ["q1"]
bina = Automaton(_states, _alphabet, _transitions, _q0, _F)

print(f"El Autómata 02: que determina un número binario que es múltiplo de 2")
print(f"Tamaño del alfabeto: {len(bina.alphabet)}")
print(bina.alphabet)
print(f"Cantidad de nodos: {len(bina.states)}")
print(bina.states)
print(f"Cantidad de transiciones: {len(bina.transitions)}")
print(bina.transitions)
print(f"El autómata es completo? >> {bina.isComplete()}")
print(f"El autómata es determinista? >> {bina.isDeterministic()}")
print(f"Pruebas:")
_test = ["0", "1", "10", "111", "101", "110", "1001", "1010"]
for i in _test:
    print(f"Prueba: {i} >> {bina.process(i)}")

# ======================================
# Example 03: Only binary numbers that start with 1 and end with 0
# ======================================
print("="*20)
_states = ["q0", "q1", "q2", "q3"]
_alphabet = ["0", "1"]
_transitions = [
    ("q0", "q1", "0")
]

_transitions = _transitions + [
    ("q1", "q1", i) for i in _alphabet
]

_transitions = _transitions + [
    ("q0", "q2", "1")
]

_transitions = _transitions + [
    ("q2", "q3", "0")
]

_transitions = _transitions + [
    ("q2", "q2", "1")
]

_transitions = _transitions + [
    ("q3", "q2", "1")
]

_transitions = _transitions + [
    ("q3", "q3", "0")
]

_q0 = "q0"
_F = ["q3"]
bina_v2 = Automaton(_states, _alphabet, _transitions, _q0, _F)
print(f"El Autómata 03: que determina un número binario empieza por 1 y termina en 0")
print(f"Tamaño del alfabeto: {len(bina_v2.alphabet)}")
print(bina_v2.alphabet)
print(f"Cantidad de nodos: {len(bina_v2.states)}")
print(bina_v2.states)
print(f"Cantidad de transiciones: {len(bina_v2.transitions)}")
print(bina_v2.transitions)
print(f"El autómata es completo? >> {bina_v2.isComplete()}")
print(f"El autómata es determinista? >> {bina_v2.isDeterministic()}")
print(f"Pruebas:")
_test = ["0", "1", "10", "111", "11001100000", "110011001", "1111110", "111111", "1000001"]
for i in _test:
    print(f"Prueba: {i} >> {bina_v2.process(i)}")

