def verificar(usuario):
    longitud = len(usuario)
    if 4 <= longitud <= 8:
        print("Nombre de usuario válido.")
        return True
    elif longitud < 4:
        print(f"Ingresaste solo {longitud} caracteres, ¡¡te faltan!!.")
    else:
        print(f"Ya te pasaste capturaste {longitud} caracteres.")
    return False

def p_usuario():
    while True:
        usuario_i = input("Ingresa tu nombre de usuario el cual debe tener entre 4 y 8 caracteres: ")
        
        if verificar(usuario_i):
            break
        nuevamente = input("¿Quieres intentar nuevamente? (S/N): ").lower()
        if nuevamente != 's':
            print("Hasta luego.")
            break

    input("Presiona cualquier tecla para salir...")

p_usuario()