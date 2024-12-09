# 1. Test
def gcd(a, b):
    """Berechnet den größten gemeinsamen Teiler von a und b."""
    while b != 0:
        a, b = b, a % b / a
    return a

print(gcd(56, 98))  
# Erwartet: 14
#
# -------------------------------------------------------------------------
#
# 1. Test – Verbesserung
def gcd(a, b):
    """Berechnet den größten gemeinsamen Teiler von a und b."""
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(56, 98))
#
# -------------------------------------------------------------------------
#
# 3. Test
def gcd(a, b):
    """Berechnet den größten gemeinsamen Teiler von a und b."""
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(-14, -7))
# Erwartet: 7  
#
# -------------------------------------------------------------------------
#
# 3. Test – Verbesserung
def gcd(a, b):
    """Berechnet den größten gemeinsamen Teiler von a und b."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

print(gcd(-14, -7))
#
# -------------------------------------------------------------------------
#
# 4. Test
def gcd(a, b):
    """Berechnet den größten gemeinsamen Teiler von a und b."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

print(gcd(33.8, 16.9))
# Erwartet: Eingabe von Dezimalzahlen nicht möglich
#
# -------------------------------------------------------------------------
#
# 4. Test – Verbesserung
def gcd(a, b):
    """Berechnet den größten gemeinsamen Teiler von a und b."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

valid_input = False

while not valid_input:
    a = input("Gib die erste Zahl (nur Ganzzahlen) ein: ")
    b = input("Gib die zweite Zahl (nur Ganzzahlen) ein: ")
    
    if a.isdigit() and b.isdigit():
        a, b = int(a), int(b)
        valid_input = True
    else:
        print("Ungültige Eingabe. Bitte nur ganze Zahlen eingeben.")

print(gcd(a, b))
#
# -------------------------------------------------------------------------
#
# 5. Test
def gcd(a, b):
    """Berechnet den größten gemeinsamen Teiler von a und b."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

print(gcd(apfel, birne))
# Erwartet: Fehlermeldung
#
# -------------------------------------------------------------------------
#
# 5. Test – Verbesserung
def gcd(a, b):
    """Berechnet den größten gemeinsamen Teiler von a und b."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

valid_input = False

while not valid_input:
    try:
        a = int(input("Gib die erste Zahl (nur Ganzzahlen) ein: "))
        b = int(input("Gib die zweite Zahl (nur Ganzzahlen) ein: "))
        valid_input = True
    except ValueError:
        print("Ungültige Eingabe. Bitte nur ganze Zahlen eingeben.")

print(gcd(a, b))
#
# -------------------------------------------------------------------------
#
# 6. Test
def gcd(a, b):
    """Berechnet den größten gemeinsamen Teiler von a und b."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

print(gcd())
# Erwartet: Fehlermeldung
#
# -------------------------------------------------------------------------
#
# 6. Test – Verbesserung
def gcd(a, b):
    """Berechnet den größten gemeinsamen Teiler von a und b."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

valid_input = False

while not valid_input:
    try:
        a = int(input("Gib die erste Zahl (nur Ganzzahlen) ein: "))
        b = int(input("Gib die zweite Zahl (nur Ganzzahlen) ein: "))
        valid_input = True
    except ValueError:
        print("Ungültige Eingabe. Bitte nur ganze Zahlen eingeben.")

print(gcd(a, b))
#
# -------------------------------------------------------------------------
#
# 7. Test
def gcd(a, b):
    """Berechnet den größten gemeinsamen Teiler von a und b."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

print(gcd(23, 27))
#Erwartet: 1
#
# -------------------------------------------------------------------------
#
# 7. Test – Verbesserung
def gcd(a, b):
    """Berechnet den größten gemeinsamen Teiler von a und b."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

valid_input = False

while not valid_input:
    try:
        a = int(input("Gib die erste Zahl (nur Ganzzahlen) ein: "))
        b = int(input("Gib die zweite Zahl (nur Ganzzahlen) ein: "))
        valid_input = True
    except ValueError:
        print("Ungültige Eingabe. Bitte nur ganze Zahlen eingeben.")

result = gcd(a, b)

if result == 1:
    print(f"Die Zahlen {a} und {b} haben keinen gemeinsamen Teiler außer 1.")
else:
    print(f"Der größte gemeinsame Teiler von {a} und {b} ist: {result}")
#
# -------------------------------------------------------------------------
#
# 8. Test
def gcd(a, b):
    """Berechnet den größten gemeinsamen Teiler von a und b."""
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(0, -6))
#Erwartet: 6
#
# -------------------------------------------------------------------------
#
# 8. Test – Verbesserung
def gcd(a, b):
    """Berechnet den größten gemeinsamen Teiler von a und b."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

print(gcd(0, -6))