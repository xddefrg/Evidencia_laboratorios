grupo1 = ["Ana", "Carlos", "Laura", "Ana"]
grupo2 = ["Pedro", "Laura", "Carlos", "Sofía"]
participantes = set(grupo1) | set(grupo2)

print("Participantes:", participantes)
print("Personas diferentes:", len(participantes))

participantes.add("Andrés")
print("Después de agregar a Andrés:", participantes)

participantes.discard("Laura")
print("Después de eliminar a Laura:", participantes)

print("Cantidad final:", len(participantes))