esta_inscrito = False
tiene_documento = True

if esta_inscrito and tiene_documento:
    print("Puede ingresar.")
else:
    print("No cumple todos los requisitos.")
    
#operador or
tiene_carnet = False
tiene_autorizacion = False
if tiene_carnet or tiene_autorizacion:
 print ("puede ingresar")
else:
    print ("no puede ingresar")
#operador not
bloqueado = True
if not bloqueado:
    print("La cuenta esta habilitada")
else:
    print ("la cuenta esta bloqueada")