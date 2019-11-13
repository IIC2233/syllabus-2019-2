# IIC2233 - Programación Avanzada

* [Versión inicial](https://github.com/IIC2233/syllabus/tree/9b8008f5f121cb9238ac823a2ff9a027371db11b) (3 de agosto)
* [Actualización 30/10](https://github.com/IIC2233/syllabus/tree/ba07be83eefa94df567652058f5b1293a26b5714): Actualización del cálculo del promedio ponderado de actividades en clases (**AC**) y creación de la **actividad recuperativa (AR)** y alternativas a la tercera actividad sumativa
* Actualización 13/11: Actualización del cálculo del promedio ponderado de las tareas (**T**) y se agrega código para explicar cálculo de notas

## Evaluación

1. Las evaluaciones serán efectuadas por medio de actividades prácticas en clases y tareas. Se calculará **la nota del curso NC** como:

    **NC =  0.6xT + 0.4xAC**

    Donde **T** es el promedio ponderado de las tareas y **AC** es el promedio de las actividades en clases.



2.  El **promedio ponderado de las tareas (T)** se calculará eliminando de la ponderación la tarea que perjudique más tu promedio. Para esto puedes probar calculando todos tus promedios posibles (es decir, tu nota original, luego sin la T0, sin la T1, y así) y quedandote con la mejor nota. Para entender cómo calcularemos tu nota puedes utilizar el siguiente código:
    
    ```python
    # Escribe aqui tus notas/posibles notas con dos decimales
    T0 = 3.57
    T1 = 5.56
    T2 = 4.85
    T3 = 6.21
    
    # Calculo de la nota
    notas = [T0, T1, T2, T3]
    pesos = [1, 2, 4, 5]
    
    if __name__ == '__main__':
        # Promedios posibles
        opciones = list()
    
        # Suma con pesos de las notas de tareas
        total = 0
        for nota, peso in zip(notas, pesos):
            total += nota * peso
    
        # Promedio sin eliminar ninguna tarea
        opciones.append(round(total / 12, 2))
    
        # Calculo de promedios eliminando cada nota
        for i in range(4):
            nueva_nota = round((total - notas[i] * pesos[i]) / (12 - pesos[i]), 2)
            opciones.append(nueva_nota)
    
        # Calculo antes de la actualización
        print(f"Tu promedio antiguo hubiera sido: {round(total / 12, 2)}")
        # Calculo con la actualización (mejor nota posible eliminando una tarea)
        print(f"Tu nuevo promedio de tareas es: {round(max(opciones), 2)}")
    ```
    
3. El **promedio ponderado de las actividades en clases (AC)** se calculará con 4 notas, de las cuales se considerarán solo las mejores tres. En lugar de tener 4 actividades sumativas, se realizarán 3, ya que no se evaluará la tercera actividad sumativa ("Input/Output y serialización").

   En lugar de esta tercera sumativa, se realizará una **actividad recuperativa (AR)** en el horario de examen del curso. Los contenidos específicos a evaluar, al igual que la fecha y hora de la evaluación, se anunciarán con un tiempo razonable de anticipación. Sin embargo, esta evaluación considerará solo las actividades formativas del curso.

   Para mantener la regla que permite borrar la peor nota en actividades sumativas, en lugar de la nota **ACS<sub>3</sub>** se tendrá **la mejor de las siguientes notas**:

   * El promedio de las otras 3 actividades sumativas (**XACS**)
   * ó la nota de la actividad recuperativa **AR** (explicada en el párrafo anterior),

   quedando **ACS<sub>3</sub> = MAX(XACS, AR)** y calculando la nota **AC** como se hacía originalmente (**AC** = ((**ACS<sub>1</sub> + ACS<sub>2</sub> + ACS<sub>3</sub> + ACS<sub>4</sub>**) - **min(ACS)**) / 3).

   Para entender cómo calcularemos tu nota puedes utilizar el siguiente código:

   ```python
   # Escribe aqui tus notas/posibles notas
   ACS1 = 3.57
   ACS2 = 5.56
   ACS4 = 4.85
   AR = 6.25
   
   if __name__ == '__main__':
       # Promedio actividades
       XACS = round((ACS1 + ACS2 + ACS4) / 3)
   
       # Nota de la actividad sumativa reemplazada (ACS3)
       ACS3 = max(XACS, AR)
   
       # Promedio eliminando la peor nota
       notas = [ACS1, ACS2, ACS3, ACS4]
       AC = round((sum(notas) - min(notas)) / 3, 2)
   
       print(f"Tu promedio de actividades es: {AC}")
   ```

4. Adicionalmente, para aprobar el curso el alumno debe cumplir con que **NC** debe ser mayor o igual a 3.950.

5. En caso contrario, se puede acceder a un **examen de última instancia** si **NC >= 3.650**. Esta opción siempre ha estado y se explicó en la primera clase del semestre. Instancias adicionales, como un examen recuperativo, se anunciarán más adelante.

6. La inasistencia a alguna de las evaluaciones presenciales (actividad) se evalúa con nota 1.0. Sin embargo, desde ahora en adelante todas las evaluaciones serán remotas a no ser que se especifique lo contrario, por lo que no exigirán marcar asistencia.

7. Solo será aproximada la nota final **NF**, a partir de la aproximación de **NC** a un decimal. El resto de las notas serán consideradas con dos decimales.

8. Las notas de todas las evaluaciónes se publicarán en [esta planilla](https://docs.google.com/spreadsheets/d/1uCscFkTf8iTBrdsFHrWAS4I5Gu1B_IZNKQ7OBk1ukqM/edit?usp=sharing). Solo se puede acceder con cuenta UC, no se dará acceso a ninguna otra cuenta.

# Recorrección

Para recorregir alguna evaluación, se publicará oportunamente un form en el que tendrán que exponer sus motivos.

**No se aceptarán recorrecciones del tipo:** "Creo que merezco más nota" sin que haya alguna justificación de por medio.

# Foro

La página de [Issues](../../issues) se utilizará como foro para preguntas.


# Semestres Anteriores

Puedes ver los `syllabus` de los semestres anteriores en:
- [2015-1](https://github.com/IIC2233-2015-1/syllabus)
- [2015-2](https://github.com/IIC2233-2015-2/syllabus)
- [2016-1](https://github.com/IIC2233-2016-1/syllabus)
- [2016-2](https://github.com/IIC2233-2016-02/Syllabus)
- [2017-1](https://github.com/IIC2233/Syllabus-2017-1)
- [2017-2](https://github.com/IIC2233/Syllabus-2017-2)
- [2018-1](https://github.com/IIC2233/Syllabus-2018-1)
- [2018-2](https://github.com/IIC2233/Syllabus-2018-2)
- [2019-1](https://github.com/IIC2233/syllabus-2019-1)

# Otros

Los contenidos, ayudantes, calendario, **cuestionario de recorrecciones** y material se encuentran en este [link](https://iic2233.github.io/).
