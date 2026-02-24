"""
FelipedelosH
2025

DEMO: Validates if mail is SPAM
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
    

# SPAM DETECTOR
email = """
Bienvenido a la OFERTA GRATIS de la PIRAMIDE.
"""

# ADF1 >> DETECT 'GRATIS'
_states = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7"]
_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","á", "é", "í", "ó", "ú"]
_transitionsADF1 = [
    ("q0", "q1", "g"),
    ("q1", "q2", "r"),
    ("q2", "q3", "a"),
    ("q3", "q4", "t"),
    ("q4", "q5", "i"),
    ("q5", "q6", "s"),
    ("q7", "q1", "g")
]

_transitionsADF1 = _transitionsADF1 + [
    ("q0", "q0", i) for i in _alphabet if i != "g"
]

_transitionsADF1 = _transitionsADF1 + [
    ("q1", "q7", i) for i in _alphabet if i != "r"
]

_transitionsADF1 = _transitionsADF1 + [
    ("q2", "q7", i) for i in _alphabet if i != "a"
]

_transitionsADF1 = _transitionsADF1 + [
    ("q3", "q7", i) for i in _alphabet if i != "t"
]

_transitionsADF1 = _transitionsADF1 + [
    ("q4", "q7", i) for i in _alphabet if i != "i"
]

_transitionsADF1 = _transitionsADF1 + [
    ("q5", "q7", i) for i in _alphabet if i != "s"
]

_transitionsADF1 = _transitionsADF1 + [
    ("q7", "q7", i) for i in _alphabet if i != "g"
]

_transitionsADF1 = _transitionsADF1 + [
    ("q6", "q6", i) for i in _alphabet
]

_q0 = "q0"
_F = ["q6"]
ADF1 = Automaton(_states, _alphabet, _transitionsADF1, _q0, _F)

for i in email:
    _symbol = str(i).lower()
    ADF1.step(_symbol)
    print(f"Analisis de la cadena {_symbol} >> estado: {ADF1.pivot}")


# ADF2 >> DETECT 'OFERTA'
_transitionsADF2 = [
    ("q0", "q1", "o"),
    ("q1", "q2", "f"),
    ("q2", "q3", "e"),
    ("q3", "q4", "r"),
    ("q4", "q5", "t"),
    ("q5", "q6", "a"),
    ("q7", "q1", "o")
]

_transitionsADF2 = _transitionsADF2 + [
    ("q0", "q0", i) for i in _alphabet if i != "o"
]

_transitionsADF2 = _transitionsADF2 + [
    ("q1", "q7", i) for i in _alphabet if i != "f"
]

_transitionsADF2 = _transitionsADF2 + [
    ("q2", "q7", i) for i in _alphabet if i != "e"
]

_transitionsADF2 = _transitionsADF2 + [
    ("q3", "q7", i) for i in _alphabet if i != "r"
]

_transitionsADF2 = _transitionsADF2 + [
    ("q4", "q7", i) for i in _alphabet if i != "t"
]

_transitionsADF2 = _transitionsADF2 + [
    ("q5", "q7", i) for i in _alphabet if i != "a"
]

_transitionsADF2 = _transitionsADF2 + [
    ("q7", "q7", i) for i in _alphabet if i != "o"
]

_transitionsADF2 = _transitionsADF2 + [
    ("q6", "q6", i) for i in _alphabet
]

_q0 = "q0"
_F = ["q6"]
ADF2 = Automaton(_states, _alphabet, _transitionsADF2, _q0, _F)

print("===============================")

for i in email:
    _symbol = str(i).lower()
    ADF2.step(_symbol)
    print(f"Analisis de la cadena {_symbol} >> estado: {ADF2.pivot}")


# UNION = AFD1 or AFD2
isSpam = ADF1.pivot in ADF1.F or ADF2.pivot in ADF2.F
print(f"Result of EMAIL >> ADF1: {ADF1.pivot in ADF1.F} || {ADF2.pivot in ADF2.F}")
print(f"is SPAM: {isSpam}")
