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
