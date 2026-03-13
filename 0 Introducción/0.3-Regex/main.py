import re

# match str to contains 'a'
words = ["andrés", "michell", "felipe", "juanita"]

_ptrn = r".*a.*"

for itterW in words:
    result = re.match(_ptrn, itterW)
    print(f"La palabra {itterW} contiene a? >> RTA: {result}")


# match if number is valid
_cc = "1059785517"
_ptrn = r"[0-9]+"
result = re.match(_ptrn, _cc)

print(f"El documento {_cc} es valido? >> RTA: {result}")


# Validates if text is in upper case.
_txts = ["LILIANA", "hogar", "MADRE"]

_ptrn = r"^[A-Z]+$"

for i in _txts:
    result = re.match(_ptrn, i)
    print(f"La palabra {i} está en mayuscula? >> RTA: {result}")
