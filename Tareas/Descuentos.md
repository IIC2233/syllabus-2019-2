# Descuentos :chart_with_downwards_trend: 

A pesar de que se pueden acumular más de 10 décimas entre todos los descuentos, el descuento final que aplica es el siguiente:

#### <center>`mín(total_descuentos_aplicados, 10) + descuento_por_entrega_atrasada + descuento_por_usar_algo_prohibido`</center>

Donde:
* `descuento_por_entrega_atrasada` es el descuento  por entregar despues del plazo indicado en el enunciado.
* `total_descuentos_aplicados` es la suma entre los descuento de PEP8, Readme, Modularización, Formato de entrega, Uso de `.gitignore` y descuentos adicionales. (Los demás descuentos que no son por atraso, ni uso de elementos prohibidos)
* `descuento_por_usar_algo_prohibido` es el descuento asociado a utilizar alguna librería o `Built-in` no autorizado. Tal como dice en cada enunciado de tarea, no se permite ninguna librería a no ser que nosotros especifiquemos lo contrario. El descuento puede ir desde 1 décima a 5 décimas dependiendo del tipo de librería prohibida utilizada.

## PEP8 (hasta 4 décimas) :pencil2: 
PEP8 es el estándar que se utiliza para programar en `Python` :snake:, por lo que es importante que se sigan las convenciones. Todo tipo de detalle sobre estas convenciones se encuentran en la [guía de estilo](https://github.com/IIC2233/contenidos-2019-2/blob/master/semana-01/1-guía-de-estilo.ipynb).

De los cuales sólo se verificarán:
1. No exceder el máximo de **100** caracteres **por línea**.
2. Uso de variables declarativas y aclarativas.
3. Uso adecuado de CamelCase y snake_case.
4. Espacio después de la coma (",").
5. Uso de espacios para indentación y **no** de tabulaciones. 
6. Utilizar correctamente los `import` (no hacer `import *`). Para más información de cómo importar archivos revisar [los contenido del curso](https://github.com/IIC2233/contenidos-2019-2/blob/master/semana-01/2-modularización.ipynb).

La cantidad de décimas a descontar será la siguiente (acorde a lo establecido arriba):
- **2 décimas** si no se cumple _sólo_ 1
- **3 décimas** si no se cumplen 2
- **4 décimas** si no se cumplen 3 _o más_

La búsqueda de estos tipos de errores tampoco debe ser una búsqueda exhaustiva, pero es altamente probable que los _linters_ se los muestren. Si sólo ven _un_ error de algún tipo siendo que en el resto de los casos no ocurre, entonces se puede perdonar.

## README (1 décima) :page_facing_up: 

Si no se indica(n) los archivos principales que son necesarios para ejecutar la tarea o su ubicación dentro de su carpeta se hará este descuento.


## Modularización (5 décimas) :package: 

Se descuentan **5 décimas** si uno o más archivos exceden las **600** líneas de código.


## Formato de entrega (hasta 5 décimas) :inbox_tray: 
 1. Lenguaje vulgar (groserías) o inapropiado para el curso.
 2. Nombres o extensiones de archivos no explícitos ni declarativos.
 3. Utilizar _paths_ absolutos en una tarea en vez de _paths_ relativos. Para más información revisar [los contenidos del curso](https://github.com/IIC2233/contenidos-2019-2/blob/master/semana-01/3-paths.ipynb).
 4. No respetar lo solicitado en el enunciado, o detallado en las issues.
 5. Utilizar código de internet sin citar. 
 
Dependiendo de la gravedad de no respetarlo, el descuento de cada ítem puede ir de 1 a 5 décimas.
Los descuentos de estos ítem son acumulables hasta un máximo de 5 décimas de descuento.

## Uso de `.gitignore` (hasta 5 décimas) :hand: 

El `.gitignore` es un archivo que permite indicar cuales archivos deben ser ignorados del repositorio, es decir, que no son detectados dentro de este al momento de querer hacer `git add`. Para más información visitar [este link](https://git-scm.com/docs/gitignore).

Este descuento sólo se aplica si en el enunciado de la tarea se especifica que **utilicen el `.gitignore`** o se indica que **no deben subir algún archivo en específico**. En caso de solicitar que usen el `.gitignore`, el descuento puede ser por uno de los 3 siguientes casos:
- **5 décimas** si no está el `.gitignore` y sube las cosas de todos modos.
- **2 decimas** si no está el gitignore pero no están subidas las cosas (no se puede evaluar el correcto uso de `.gitignore`)
- **2 décimas** si sube igual los archivos a ignorar a pesar de tener el archivo `.gitignore` (no cumple con el objetivo del `.gitignore` o no lo utiliza correctamente)
- **Importante:** el `.gitignore` debe estar dentro de la carpeta (T01/, T02/ o T03/), no se aceptará que lo pongan en otra parte aunque funcione.

## Adicionales (hasta 5 décimas) :information_source:
Dependiendo de cómo esté hecha la tarea, el ayudante se puede topar con múltiples inconvenientes que impidan la corrección de la tarea o le dificulten en gran medida la revisión de esta. Es por esto que puede aplicar el descuento que considere apropiado para la situación en la que se encuentre de ser justificado.

## Des-descuento (hasta 5 décimas) :tada:

Puedes restar máximo 5 décimas de tus descuentos, las condiciones para restar estas décimas de descuento es entregar un _README.md_ que cumpla con:
* Explicitar cada ítem de la distribución del puntaje que no fueron implementados.
* Explicitar posibles errores y su solución.
* Especificar el archivo y línea donde se puede encontrar cada ítem de la distribución del puntaje que puede ser evaluado mediante la lectura de código.

Finalmente, la cantidad de décimas restadas queda a criterio del ayudante.

## Entrega atrasada (entre 5-20 décimas) :watch: 

Si se entrega la tarea atrasada se tendrá un descuento **inicial** de 5 décimas hasta un descuento de 20 décimas a las 24hrs de atraso del plazo establecido de manera lineal, con la fórmula:

### <center>5+15t/24</center>

Donde `t` está en horas (es una función **continua** y no discreta) y no se permiten entregas pasadas las 24 hrs de la hora inicial de entrega.
