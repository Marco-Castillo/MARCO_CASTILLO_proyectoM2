# Validación de usuario

#### ¿Qué hace?
Este pequeño programa te ayuda a validar un nombre de usuario asegurándose de que tenga entre 4 y 8 caracteres. 

#### ¿Cómo funciona?
el código consta de 2 funciones:
 
- Función verificar(usuario):
Esta función toma el nombre de usuario que ingresaste y verifica cuántos caracteres tiene.
	-	Si tiene entre 4 y 8 caracteres, te dirá "Nombre de usuario válido" y te dejará seguir.
	-	Si tiene menos de 4 caracteres, te dirá que te faltan algunos.
	-	Si tiene más de 8 caracteres, te dirá que ya te pasaste con tantos caracteres.

- Función p_usuario(): la Interacción es mas o menos así
	- Paso 1: Te pide que ingreses un nombre de usuario que tenga entre 4 y 8 caracteres.
	- Paso 2: Luego llama a la función verificar() para ver si tu nombre de usuario está en el rango correcto.
	- Paso 3: Si tu nombre de usuario está bien, termina y te dice que ya puedes salir.
	- Paso 4: Si tu nombre de usuario es demasiado corto o largo, te pregunta si quieres volver a intentarlo
	- Paso 5: Si decides no volver a intentar (diciendo "N" o algo diferente de "S"), el programa te dice "Hasta luego" y se termina.
