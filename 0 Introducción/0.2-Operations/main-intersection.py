"""
FelipedelosH
2026

DEMO: Validates Password
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

_PASSWORD_ = "Kmzwa8awaa"
_alphabet_number_str = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
_alphabet_lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","á", "é", "í", "ó", "ú"]
_alphabet_upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","Á", "É", "Í", "Ó", "Ú"]
    
# ADF1 >> UPPER CASE DETECTOR
_states = ["q0", "q1"]
_alphabet = _alphabet_number_str + _alphabet_lower_case + _alphabet_upper_case
_transitionsADF1 = [
    ("q0", "q0", i) for i in _alphabet_number_str + _alphabet_lower_case
]

_transitionsADF1 = _transitionsADF1 + [
    ("q0", "q1", i) for i in _alphabet_upper_case
]

_transitionsADF1 = _transitionsADF1 + [
    ("q1", "q1", i) for i in _alphabet_number_str + _alphabet_lower_case + _alphabet_upper_case
]

_q0 = "q0"
_F = ["q1"]
ADF1 = Automaton(_states, _alphabet, _transitionsADF1, _q0, _F)


#ADF2 >> LOWER CASE DETECTOR
_states = ["q0", "q1"]
_alphabet = _alphabet_number_str + _alphabet_lower_case + _alphabet_upper_case
_transitionsADF2 = [
    ("q0", "q0", i) for i in _alphabet_number_str + _alphabet_upper_case
]

_transitionsADF2 = _transitionsADF2 + [
    ("q0", "q1", i) for i in _alphabet_lower_case
]

_transitionsADF2 = _transitionsADF2 + [
    ("q1", "q1", i) for i in _alphabet_number_str + _alphabet_lower_case + _alphabet_upper_case
]

_q0 = "q0"
_F = ["q1"]
ADF2 = Automaton(_states, _alphabet, _transitionsADF2, _q0, _F)


#ADF3 >> NUMBER DETECTOR
_states = ["q0", "q1"]
_alphabet = _alphabet_number_str + _alphabet_lower_case + _alphabet_upper_case
_transitionsADF3 = [
    ("q0", "q0", i) for i in _alphabet_lower_case + _alphabet_upper_case
]

_transitionsADF3 = _transitionsADF3 + [
    ("q0", "q1", i) for i in _alphabet_number_str
]

_transitionsADF3 = _transitionsADF3 + [
    ("q1", "q1", i) for i in _alphabet_number_str + _alphabet_lower_case + _alphabet_upper_case
]

_q0 = "q0"
_F = ["q1"]
ADF3 = Automaton(_states, _alphabet, _transitionsADF3, _q0, _F)


# ADF4 >> LEN VALIDATOR
_states = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7"]
_alphabet = _alphabet_number_str + _alphabet_lower_case + _alphabet_upper_case
_transitionsADF4 = [
    ("q0", "q1", i) for i in _alphabet_number_str + _alphabet_lower_case + _alphabet_upper_case
]

_transitionsADF4 = _transitionsADF4 + [
    ("q1", "q2", i) for i in _alphabet_number_str + _alphabet_lower_case + _alphabet_upper_case
]

_transitionsADF4 = _transitionsADF4 + [
    ("q2", "q3", i) for i in _alphabet_number_str + _alphabet_lower_case + _alphabet_upper_case
]

_transitionsADF4 = _transitionsADF4 + [
    ("q3", "q4", i) for i in _alphabet_number_str + _alphabet_lower_case + _alphabet_upper_case
]

_transitionsADF4 = _transitionsADF4 + [
    ("q4", "q5", i) for i in _alphabet_number_str + _alphabet_lower_case + _alphabet_upper_case
]

_transitionsADF4 = _transitionsADF4 + [
    ("q5", "q6", i) for i in _alphabet_number_str + _alphabet_lower_case + _alphabet_upper_case
]

_transitionsADF4 = _transitionsADF4 + [
    ("q6", "q7", i) for i in _alphabet_number_str + _alphabet_lower_case + _alphabet_upper_case
]

_transitionsADF4 = _transitionsADF4 + [
    ("q7", "q7", i) for i in _alphabet_number_str + _alphabet_lower_case + _alphabet_upper_case
]

_q0 = "q0"
_F = ["q7"]
ADF4 = Automaton(_states, _alphabet, _transitionsADF4, _q0, _F)


for i in _PASSWORD_:
    _symbol = i

    print(f"Analisis del Simbolo: {_symbol}")
    ADF1.step(_symbol)
    print(f"Estado de Autómata ADF1 : {ADF1.pivot}")
    ADF2.step(_symbol)
    print(f"Estado de Autómata ADF2 : {ADF2.pivot}")
    ADF3.step(_symbol)
    print(f"Estado de Autómata ADF3 : {ADF3.pivot}")
    ADF4.step(_symbol)
    print(f"Estado de Autómata ADF4 : {ADF4.pivot}")


# INTERSECTION = ADF1 AND ADF2 AND ADF3
_isValidPassword = ADF1.pivot in ADF1.F and ADF2.pivot in ADF2.F and ADF3.pivot in ADF3.F and ADF4.pivot in ADF4.F
print(f"Resultado: la contraseña: {_PASSWORD_} es valida: {_isValidPassword}")
