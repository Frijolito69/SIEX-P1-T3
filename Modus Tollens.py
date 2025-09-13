def modus_tollens(P, Q):
    """
    Aplica Modus Tollens:
    Si P implica Q, y Q es falso, entonces P es falso.
    """
    if not Q:  # Negación de Q
        return not P  # Entonces no P
    return None

# "Si llueve, la calle está mojada."
P = True   # Llovió
Q = False  # La calle no está mojada
resultado = modus_tollens(P, Q)

print("\nEjemplo Modus Tollens:")
print(f"Premisa: Si llueve, la calle se moja. Calle mojada = {Q}")
print(f"Conclusión: Llovió = { resultado}")
