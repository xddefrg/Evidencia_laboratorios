edad = int(input("introduce tu edad"))
autorizacion = input("¿tienes autorizacion? (si/no):").lower
if edad >= 18:
    print("acceso permitido.")
elif autorizacion == "si":
    print("acceso permitido con autorizacion")
else:
    print ("acceso denegado.")
    