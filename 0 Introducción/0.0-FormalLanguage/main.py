"""
FelipedelosH
2025

Formal Language + My First Automaton
"""
class Automaton:
    def __init__(self, states, alphabet, transitions, q0, F):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.q0 = q0
        self.F = F
        self.pivot = q0

    def reset(self):
        self.pivot = self.q0

    def step(self, s):
        for (k,v,n) in self.transitions:
            if k == self.pivot and n == s:
                self.pivot = v
                return True
        return False

    def process(self, word):
        self.reset()
        for symbol in word:
            if not self.step(symbol):
                return False
        return self.pivot in self.F


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

_chain0 = "andrés"
_chain1 = "michell"
_chain2 = "felipe"
_chain3 = "juanita"
# language
_chains = [_chain0, _chain1, _chain2, _chain3]

for i in _chains:
    a.process(i)
    print(f"Analisis de la cadena {i} >> estado: {a.pivot}")
