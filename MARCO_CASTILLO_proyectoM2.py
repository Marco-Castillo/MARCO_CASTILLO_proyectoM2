def verificar(usuario):
    # verifica la longitud de caracteres ingresados
    longitud = len(usuario)
    # se verifica si la longitud esta entre 4 y 8 caracteres
    if 4 <= longitud <= 8:
        print("Nombre de usuario válido.")
        # devuelve si la peticion es verdadera
        return True
    # condicion para cuando los caracteres son menores de 4
    elif longitud < 4:
        print(f"Ingresaste solo {longitud} caracteres, ¡¡te faltan!!.")
    # Condicion para cuando rebasa los 8 caracteres
    else:
        print(f"Ya te pasaste capturaste {longitud} caracteres.")
    return False
    
def p_usuario():
    #bucle para ingresar el numero de usuario hasta que sea correcto o el cliente decida salir
    while True:
        usuario_i = input("Ingresa tu nombre de usuario el cual debe tener entre 4 y 8 caracteres: ")
        # Llama a la funcion verificar para checar si cumple con la longitud
        if verificar(usuario_i):
            #en caso de que se compla rompe el bucle
            break
        #en caso de que verificar no se cumpla, pregunta al usuario si quiere intentarlo de nuevo
        nuevamente = input("¿Quieres intentar nuevamente? (S/N): ").lower()
        #si la entrada es diferente a 's' sale del bucle y manda un mensaje
        if nuevamente != 's':
            print("Hasta luego.")
            break
    # se espera que el usuario presione enter para salir
    input("Presiona enter para salir...")

# llama a la funcion principal para incial el programa
p_usuario()