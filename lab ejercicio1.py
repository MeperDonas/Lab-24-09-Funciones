def validar(email):
    b = a.count("@")
    if b == 1:
        return True
    return False
    
a=input("Introucir tu email: ")
if validar(a):
    print("Direccion valida")
else:
    print("Direccion invalida")
    print("Por favor ingrese su email con @")