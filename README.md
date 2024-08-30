# Validación de usuario y 

#### ¿Qué hace?
Este programa está dividido en dos partes. La primera te ayuda a verificar que el nombre de usuario que ingreses tenga entre 4 y 8 caracteres, para que sea válido. La segunda parte te pide dos números, X e Y, y te dice en cuál de los cuatro cuadrantes del plano cartesiano cae el punto que forman esos números.

#### ¿Cómo funciona?
el código consta de 2 funciones que se ejecuta una tras otra
 
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

 - Funcion ocuadrante():
 	- Utiliza un diccionario para asociar los signos de las coordenadas X,Y con los cuadrantes del plano cartesiano
  	- Primero toma las coordenadas de X e Y de la tubla que recibe como entrada
   	- Si el usuario coloca una coordenada con valor 0 arroja un mensaje de error y no puede avanzar debido al bucle que se coloca
   	- si las coordenadas son correctas, la función indica en que cuadrante se coloca el punto de los datos ingresados por el usuario y devuelve el resultado

Función dcuadrante():

-   Utiliza un bucle para pedirte que ingreses dos números: uno para X y otro para Y.
-   Si alguno de los dos números (o ambos) es 0, el programa te avisará y te pedirá que ingreses otros valores diferentes de 0.
-   Una vez ingreses números válidos, el programa te dirá en qué cuadrante se encuentra el punto, y luego te pedirá que presiones Enter para finalizar.

### Opinión del bootcamp
Me han ayudado muchísimo a entender mejor cómo funciona la programación en este lenguaje, y me siento muy cómodo con lo que he aprendido hasta ahora. Seguiré aprovechando cada una de sus clases, a un que no las tomo en vivo siempre estoy al pendiente. ¡Gracias!
   
