def berechne_potenz(basis, exponent):
  """Berechnet die Potenz einer Zahl.

  Args:
    basis: Die Basis der Potenz.
    exponent: Der Exponent der Potenz.

  Returns:
    Die berechnete Potenz.
  """

  return basis ** exponent

# Benutzer nach Basis und Exponent fragen
basis = float(input("Gib die Basis ein: "))
exponent = '2'

# Potenz berechnen und ausgeben
ergebnis = berechne_potenz(basis, exponent)
print(basis, "hoch", exponent, "ist", ergebnis)

