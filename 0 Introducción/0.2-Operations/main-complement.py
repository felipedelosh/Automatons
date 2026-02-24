"""
FelipedelosH
2026

DEMO: Validates if product is with discount.

DISCOUNT ONLY IN OLD PRODUCTS
N: NEW
V: OLD
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
    
class Product:
    def __init__(self, id, nombre, code):
        self.id = id
        self.nombre = nombre
        self.code = code


_states = ["q0", "q_new", "q_old"]
_alphabet = ["CN", "CV", "PN", "PV", "ZN", "ZV"]
_transitions = [
    ("q0", "q_new", "CN"),
    ("q0", "q_old", "CV"),
    ("q0", "q_new", "PN"),
    ("q0", "q_old", "PV"),
    ("q0", "q_new", "ZN"),
    ("q0", "q_old", "ZV"),
]
_q0 = "q0"
_F = ["q_new"]

# CLSY NEW PRODUCTS
ADF1 = Automaton(_states, _alphabet, _transitions, _q0, _F)

productos = [
    Product(1, "Camisa GUCCI", "CN"), 
    Product(2, "Camisa POLO", "CV"),
    Product(3, "Pantalon JEAN", "PN"),
    Product(4, "Pantalon MILITAR", "PV"),
    Product(5, "Zapatos Nike", "ZN"),
    Product(6, "Zapatos Adidas", "ZV"),
]

for prod in productos:
    _symbol = prod.code

    ADF1.reset()
    ADF1.step(_symbol)

    _discount = ADF1.pivot not in ADF1.F

    if _discount:
        print(f"El producto: {prod.nombre} Tiene un 10% de descuento.")
