# Optimizador de horarios del CEITBA
El objetivo de este proyecto es obtener una lista (top 3) de combinaciones de horarios en donde sea poco probable que quede todo junto en una semana.
 
 
# Lógica
Actualmente si se quiere utilizar el código simplemente hay que decirle al programa que combinación uno desea obtener. Su cuatrimestre "ideal". El vector ideal está compuesto por la siguiente información:
- cantidad de parciales en la primera semana
- cantidad de parciales en la segunda semana
- cantidad de parciales en la tercera semana
- cantidad de parciales (2) en la primera semana
- cantidad de parciales (2) en la segunda semana
- cantidad de parciales (2) en la tercera semana
- cantidad de bloques de 3 horas durante la mañana
- cantidad de bloques de 3 horas durante la mediodia
- cantidad de bloques de 3 horas durante la tarde
 
En el archivo materias.json se encuentra toda la información de las materias que están recopiladas. Estas tienen la siguiente información:
```
"(xx.xx)": [
        {
            "Nombre": "",
            "Parcial en semana 1": 0,
            "Parcial en semana 2": 0,
            "Parcial en semana 3": 0,
            "Parcial 2 en semana 1": 0,
            "Parcial 2 en semana 2": 0,
            "Parcial 2 en semana 3": 0,
            "Clases a la manana": 0,
            "Clases al mediodia": 0,
            "Clases a la tarde": 0,
            "Creditos": 0,
            "Correlativas": [
                "(yy.yy)",
                "(zz.zz)"
            ]
        }
    ]
```
Al ejecutar el código se obtienen todas las materias del archivo materias.json, se descartan las que especificó el usuario y luego las que son correlativas de materias no descartadas.
Una vez que tenemos la lista con todas las materias que queremos contemplar en el optimizador se realiza una [combinación sin repetición](https://docs.python.org/3/library/itertools.html#itertools.combinations).
 
![Ecuación utilizada](https://economipedia.com/wp-content/uploads/combinatoria-sin-repetici%C3%B3n.jpg "Ecuación utilizada")
 
Luego se arma una lista de vectores que contienen la informacion de todas las materias en esa combinacion en particular y se suman a un unico vector (vectorTotal), luego se utiliza la [formula del producto escalar](https://economipedia.com/definiciones/angulo-entre-dos-vectores.html) en donde obtenemos el angulo entre dos vectores (en este caso seria entre el vector total y el ideal al que apuntamos).
 
![Ecuación utilizada](https://economipedia.com/wp-content/uploads/Producto-escalar-geome%CC%81trico.png "Ecuación utilizada")
 
El resultado de esta ecuación se guarda y se compara con los siguientes vectores para armar el top 3.
 
### Posibles problemas
- Es probable que al principio no sea muy preciso debido a la falta de datos, pero a medida que pasa el tiempo es seguro asumir que las fechas de parciales por materia tendrían una distribución normal a menos que el contenido varíe mucho/cambie quien organiza la clase. Con el objetivo de aumentar la precisión se podría implementar que cada materia tenga los datos expresados en %. Osea que es la cantidad de veces que cayó en la primera semana el parcial / la cantidad de cuatrimestres de muestra que se tienen en la base de datos.
- TBD
 
# Estado actual del proyecto:
### Combinador de horarios.
- [x] Generar las listas y evitar que las combinaciones se repitan.
- [x] Evitar que se excedan los créditos especificados por el usuario.
- [x] Enviar la lista al optimizador.
- [x] Guardar top tres de los ángulos y sus respectivas listas de materias.
- [x] Que no tome en cuenta las materias que el usuario especifica.
- [x] Que excluya las que tienen correlativas sin cursada aprobada.
- [ ] Que avise si hay una combinación que contiene una correlativa con cursada aprobada. (web)
 
### Optimizador.
- [x] Recibir dos Inputs, lista de materias y Vector ideal.
- [x] Extraer las materias de la lista y armar el vector Total.
- [x] Calcular el ángulo entre esos dos vectores.
- [x] Devolver el ángulo al combinador.
 
### Interfaz temporal
- [ ] Que sea capaz de agregar mas materias al archivo de materias.json
- [ ] Que liste todas las materias en bloques y que permita modificarlas de manera intuitiva
- [ ] Que acepte archivos csv
- [ ] Que haga un promedio de todos los datos del csv y que le avise al usuario por si se repiten
 
 
## Objetivos a futuro (después de finales).
- [ ] Que distinga entre turno tarde, mañana y mediodía (tomando los datos de el Vector ideal).
- [ ] Que verifique cuales son correlativas así las elimina del sistema.
- [ ] Que liste los profesores que dieron clase en esa comision
- [ ] Que se pueda filtrar por carrera para no tener que excluir lo que no es de otras carreras.
- [ ] \(Opcional) Que tome en cuenta la metodología del examen (Si es grupal o son TPs).
- [ ] Interfaz web.
 
 
## La interfaz web
 
La idea sería que el usuario inicie sesión con su mail ITBA y que pueda acceder a toda su información (votos en propuestas CEITBA y progreso en la materia), una vez dentro, en la sección de optimizador de horarios vería la página.
 
 
### MVP.
- [ ] Que diga una lista básica de las materias en las que conviene anotarse.
- [ ] Que exista una pagina para cargar más materias así no hay que modificar el json manualmente.
- [ ] Que se asegure que el usuario no ponga los datos mal (ie. pone una "e" en donde va un int).
 
### UI.
- [ ] Que obtenga los datos del usuario de su perfil y que pueda agregar más materias a lo aprobado.
- [ ] Que el usuario diga que materias curso así las excluye de la lista y que guarde en su perfil.
- [ ] En caso de que exista una combinación con una materia sin el final aprobado que aparezca la opción de excluirlo de los resultados.
- [ ] Eso o que simplemente se pueda filtrar y excluir a las materias sin final aprobado.
- [ ] En caso de que los datos de esa materia no existan que el usuario las pueda ingresar.
- [ ] Pagina para cargar datos.
 
### Interno CEITBA.
- [ ] Si se ingresa la información se le avisa a un moderador que se cargaron datos y que si puede, que verifique que las fechas estén bien cargadas.
