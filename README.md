# Optimizador de horarios del CEITBA
La idea sería armar un código (Próximamente una página web) en donde uno carga los datos necesarios de las materias y el algoritmo se encarga de generar una lista con las clases en donde uno le conviene anotarse.
 
Actualmente tiene los datos cargados de las materias que estoy cursando ahora y curse y solo sirve para verificar y crear la mejor combinación de entre ellas.
 
# Lógica
Se arma una lista de vectores que contienen la informacion de todas las materias y se suman a un unico vector, luego se utiliza la [formula del producto escalar](https://economipedia.com/definiciones/angulo-entre-dos-vectores.html) en donde obtenemos el angulo entre dos vectores (en este caso seria entre el vector total y el ideal al que apuntamos).
 
![Ecuación utilizada](https://economipedia.com/wp-content/uploads/Producto-escalar-geome%CC%81trico.png "Ecuación utilizada")
 
## TODO:
### Combinador de horarios.
- [x] Generar las listas y evitar que las combinaciones se repitan.
- [x] Evitar que se excedan los créditos especificados por el usuario.
- [x] Enviar la lista al optimizador.
- [x] Guardar top tres de los ángulos y sus respectivas listas de materias.
- [ ] Que no tome en cuenta las materias que el usuario especifica.
- [ ] Que excluya las que tienen correlativas sin cursada aprobada.
- [ ] Que avise si hay una combinación que contiene una correlativa con cursada aprobada.
 
### Optimizador.
- [x] Recibir dos Inputs, lista de materias y Vector ideal.
- [x] Extraer las materias de la lista y armar el vector Total.
- [x] Calcular el ángulo entre esos dos vectores.
- [x] Devolver el ángulo al combinador.
 
## Objetivos a futuro (después de finales).
- [ ] Que distinga entre turno tarde, mañana y mediodía (tomando los datos de el Vector ideal).
- [ ] Que verifique cuales son correlativas así las elimina del sistema.
- [ ] \(Opcional) Que tome en cuenta la metodología del examen (Si es grupal o son TPs).
- [ ] Interfaz web.
 
 
# La interfaz web
 
La idea sería que el usuario inicie sesión con su mail ITBA y que pueda acceder a toda su información (votos en propuestas CEITBA y progreso en la materia), una vez dentro, en la sección de optimizador de horarios vería la página.
 
## TODO:
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
 
 
 
 

