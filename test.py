def ist_primzahl(zahl):
  """Überprüft, ob eine Zahl eine Primzahl ist.

  Args:
    zahl: Die zu überprüfende Zahl.

  Returns:
    True, wenn die Zahl eine Primzahl ist, andernfalls False.
  """

  if zahl <= 1:
    return False
  if zahl <= 3:
    return True
  if zahl % 2 == 0 or zahl % 3 == 0:
    return False
  i = 5
  while i * i <= zahl:
    if zahl % i == 0 or zahl % (i + 2) == 0:
      return False
    i += 6
  return True

def finde_hoechste_primzahl(obergrenze):
  """Findet die höchste Primzahl bis zu einer gegebenen Obergrenze.

  Args:
    obergrenze: Die obere Grenze der Suche.

  Returns:
    Die höchste gefundene Primzahl.
  """

  hoechste_primzahl = 0
  for zahl in range(obergrenze, 1, -1):
    if ist_primzahl(zahl):
      hoechste_primzahl = zahl
      break
  return hoechste_primzahl

# Hauptprogramm
obergrenze = 1000000
hoechste_primzahl = finde_hoechste_primzahl(obergrenze)
print("Die höchste Primzahl unter", obergrenze, "ist:", hoechste_primzahl)
