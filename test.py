def potenziere_mit_zwei(zahl):
  """Potenziert eine Zahl mit 2.

  Args:
    zahl: Die Zahl, die potenziert werden soll.

  Returns:
    Das Ergebnis der Potenzierung.
  """

  return zahl ** 2

# Benutzer nach einer Zahl fragen
eingabe = float(input("Gib eine Zahl ein: "))

# Zahl mit 2 potenzieren und Ergebnis ausgeben
ergebnis = potenziere_mit_zwei(eingabe)
print("Das Quadrat von", eingabe, "ist", ergebnis)
