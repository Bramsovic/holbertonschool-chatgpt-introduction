#!/usr/bin/python3
import sys

def factorial(n):
    """Calcule la factorielle de n (n!)."""
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    """Point d'entrée principal du script."""
    if len(sys.argv) != 2:
        print("Usage : python3 script.py <nombre_entier>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        result = factorial(n)
        print(f"Factorielle de {n} : {result}")
    except ValueError as e:
        print(f"Erreur : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
