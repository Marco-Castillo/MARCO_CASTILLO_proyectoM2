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
    # se espera que el usuario presione enter para pasar al siguiente programa
    input("Presiona enter para pasar a revisar el cuadrante")

def ocuadrante(coordenadas):
    #se agrega un diccionario con la asociasion de signos con los cuadrantes
    cuadrantes = {
        (True, True): "I",
        (False, True): "II",
        (False, False): "III",
        (True, False): "IV"
    }
    #se desempaquetan las coordenadas de la tupla
    x, y = coordenadas
    # se verifica si alguno de los 2 valores es 0
    if x == 0 or y == 0:
        #imprime un mensaje indicando que no puede colocar el numero 0
        print("No puedes colocar 0, intenta de nuevo")
        return
    
    #indica el cuadrante del punto en el diccionario
    cuadrante = cuadrantes[(x > 0, y > 0)]
    #imprime el mensaje indicando en que cuadrante se encuentra el punto
    return f"El punto ({x},{y}) se encuentra en el cuadrante {cuadrante}"

    

def dcuadrante():
    #este bucle es infinito y se repetira hasta que coloquen coordenadas diferentes a 0
    while True:
        x = int(input("\nIngrese X: "))
        y = int(input("Ingrese Y: "))
        #crea una tupla con las coordenadas ingresadas
        coordenadas = (x, y)
        #llama a la funcion ocuadrante para obtener el cuadrante
        resultado = ocuadrante(coordenadas)
        #si el resultado es None significa que las coordenadas son validas
        if resultado is not None:
            #imprime el resultado
            print(resultado)
            #sale del bucle
            break
    #imprime que presione una tecla para poder salir del programa
    input("Presiona enter para salir")

#llama a la funcion principal p_usuario
p_usuario()
#llama a la funcion dcuadrante
dcuadrante()