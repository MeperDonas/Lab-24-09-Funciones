cond = "si"
def primo(num):
    for i in range(2, num):
        if num%1==0:
            return False
    return True
while cond == "si":
    numero=int(input("Ingrese un Numero: "))
    if primo(numero):
        print("Es un primo")
    else:
        print("No es primo")
    cond=input("Quieres ingresar otro Numero? ")
    if cond == "no":
        print("Hasta luego, vuelva pronto")