cond="si"
def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10 
   return cantidad
while cond=="si":
    num=int(input("ingrese un Número: "))
    un_digito=int(input("ingrese un Dígito: "))
    print("Frecuencia del dígito en el número:",frecuencia(num,un_digito))
    cond=input("quieres volver a intentar = ¿si o no?: ")
    if cond =="no":
        print("vuelve pronto amigo....(saludos desde Tibú)")

