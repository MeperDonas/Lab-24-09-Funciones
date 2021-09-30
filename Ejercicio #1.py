def valida(email): #Defino la funcion 
    tiene_arroba = False  #Variable False 
    tiene_punto = False
    for char in email:  #Ciclo for para buscar el caracter
        if char == '@':  #Primer caracter
            tiene_arroba = True  #Variable True para poder ejecutar la condicion 
        elif char == '.':  #Segundo caracter
            tiene_punto = True
    return tiene_arroba and tiene_punto  #Y retorna True si cumple con ambas variables

direccion = ''  #Agrego una variable erronea para que entre en el ciclo while
while(not valida(direccion)):  #sí el ciclo while es diferente a direccion se ejecutan las condiciones
    direccion=input("Tu email: ")
    if valida(direccion):
        print("Direccion valida")   
    else: 
        print("Direccion invalida")
        print("Vuele a ingresar el email")
#Por que hice un ciclo while? para poder darle mas opcion al usuario de seguir ingresando el correo. 

print(direccion)
print('Gracias')



    
         

       
    


     
            



