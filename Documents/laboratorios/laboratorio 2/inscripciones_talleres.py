python = {"Ana", "Carlos", "Laura", "Pedro", "Sofía"}
java = {"Carlos", "Laura", "Miguel", "Sofía", "Andrés"}

print("Al menos uno:", python | java)

print("En ambos:", python & java)

print("Solo Python:", python - java)

print("Solo Java:", java - python)

print("En un solo taller:", python ^ java)