codigos = [" p001 ", "P002", "", " p003", "  "]

codigos_limpios = [
    codigo.strip().upper()
    for codigo in codigos
    if codigo.strip() != ""
]

print("Códigos originales:", codigos)
print("Códigos normalizados:", codigos_limpios)