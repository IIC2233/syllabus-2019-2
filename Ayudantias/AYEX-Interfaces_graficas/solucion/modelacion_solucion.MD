## Modelación de solución propuesta para Ayudantía Extra: Interfaces gráficas

En este documento se detalla brevemente la modelación creada para crear un programa que responde a lo propuesto en el enunciado de la Ayudantía Extra de Interfaces gráficas.

Se implementó una separación *front-end* y *back-end* para implementar el juego propuesto. En el *front-end* se incluyen las dos ventanas pedidas: una ventana de menú (`MenuWindow`) que espera los clics del usuario y una ventana con el juego en si (`GameWindow`) que espera que el usuario juegue mediante teclas.

Al seguir la separación *front-end/back-end*, se tomó de la manera más literal posible y se dejó que las clases de las ventanas recién mencionadas solo realicen tareas visuales. De manera, que se le delega toda tarea lógica interna del programa a componentes del *back-end*. Para controlar el conteo de clics del menú, se creó la clase `CounterChecker`, mientras que para administrar las propiedades del personaje se creó la clase `Character`. Esta separación asegura alto nivel de **cohesión** en el código del programa.

Para seguir al pie de la letra la separación y conseguir el menor acoplamiento posible, se utilizó señales para comunicar cada uno de estos componentes. El siguiente diagrama muestra la dirección de la señales utilizadas entre los distintos componentes de la modelación:

![diagrama][diagrama]

[diagrama]: diagrama-componentes.png "Diagrama de componentes"

Específicamente, las funciones de las señales son:

- `MenuWindow` --> `CounterChecker`: Avisa cada vez se debe actualizar el contador interno actual. Esta señal se emite cada vez que se presiona el botón del menú.
-  `CounterChecker` --> `MenuWindow`: Avisa a la ventana que se debe actualizar su contenido. Esta señal se emite cada vez se actualiza el contador interno.
-  `MenuWindow` --> `GameWindow`: Ventana de menú avisa a ventana de juego que debe mostrarse. Esta señal se emite cuando se inicia el juego principal y se esconde el menú.
-  `GameWindow` --> `Character`: Avisa cada vez que se debe actualizar el estado del personaje. Esta señal se emite cada vez que se presiona una tecla para hacer mover el personaje.
-  `Character` --> `GameWindow`: Avisa a la ventana cada vez que se debe actualizar la imagen del personaje en la ventana. Esta señal se emite cada vez que se actualiza el estado interno del personaje.