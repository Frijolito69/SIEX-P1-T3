def modus_ponens(P, Q):
    """
    Aplica Modus Ponens:
    Si P implica Q, y P es verdadero, entonces Q es verdadero.
    """
    if P:  # Premisa P
        return Q  # Conclusión Q
    return None

# "Si estudio, apruebo."
P = True   # Estudio
Q = True   # Apruebo
resultado = modus_ponens(P, Q)

print("Ejemplo Modus Ponens:")
print(f"Premisa: Si estudio, apruebo. Estudio = {P}")
print(f"Conclusión: Aprobar = {resultado}")
