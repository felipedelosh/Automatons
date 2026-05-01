"""
FelipedelosH
2026

Automaton
"""
class Automaton:
    def __init__(self, states, alphabet, transitions, q0, F):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.q0 = q0
        self.F = F
        self.pivot = q0

    def isComplete(self):
        for state in self.states:
            for symbol in self.alphabet:
                found = False
                for (origin, _, sym) in self.transitions:
                    if origin == state and sym == symbol:
                        found = True
                        break

                if not found:
                    return False

        return True
    
    def isDeterministic(self):
        for state in self.states:
            for symbol in self.alphabet:
                count = 0
                for (origin, _, sym) in self.transitions:
                    if origin == state and sym == symbol:
                        count += 1
                        if count > 1:
                            return False
        return True
    
    def addTransition(self, origin, destination, symbol):
        self.transitions.append((origin, destination, symbol))

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
