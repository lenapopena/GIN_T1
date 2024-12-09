def is_prime(n):
    """Überprüft, ob eine Zahl eine Primzahl ist."""
    if isinstance(n, int) or n < 2:  #Überprüfung auf int und Grenzfälle
        return False
    if n == 2:  #Grenzfallprüfung -> 2 ist die einzige gerade Primzahl
        return True
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True #Wenn die obige Überprüfung nicht greift handel es sich umm eine Primzahl

# Beispiel
print(is_prime(-5))  