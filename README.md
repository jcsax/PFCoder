# PFCoder
Proyecto Final Coderhouse desarrollado por:
-Joan Camarotta: Sistema de perfiles, sistema de creación/modificación de entradas, about_us, buscador en conjunto con Juan Echecolanea, mejoras al navbar y views, creación de cards para las entradas. correciones varias y mejroas al resto de funciones.

-Juan Manuel Echecolanea: Sistema de registro/login, traducción de formularios, buscador, admin personalizado, correcciones varias y mejoras al resto de funciones.

-Juan Francisco Laborde: Correcciones y mejoras en algunas funciones. Creación de contenido para las notas.

link al video: https://youtu.be/gCDZPoakaUM

Estamos utilizando Django 4.0.4 y plantillas de bootstrap 5.2 en el requeriments.txt pueden ver las librerías instaladas.

La página se pensó como un blog de noticias: 
-Cuenta con diferentes secciones que nos permiten tanto consultar noticias como crear nuevas entradas al blog.

La primera sección "Inicio" es una página donde aparecen las noticias ultimas 4 noticias, ordenadas por fecha

La sección "Noticias" donde las mismas se encuentran clasificadas en cuatro temáticas: Entretenimiento, Salud, Deportes y Economía. Al ingresar a cada una de estas categorías nos aparecerán las noticias relativas al tema seleccionado. 

La próxima sección "Publicar", nos permite crear noticias. Estas se podrán crear mediante un formulario seleccionando el tema dentro de las categorías del Blog:
-Al hacer click para "Publicar" una noticia se despliega una pantalla donde podremos crear una nueva entrada. La misma cuenta con los campos título, autor, fecha de publicación, el cuerpo del texto, categoría e imagen.

Por ultimo existe una sección "Acerca de nosotros", que contiene un breve resumen del proyecto y los datos de los creadores de la página.

Para que la navegación sea más fluida se creó un botón de búsqueda que funciona sobre palabras clave dentro de la nota. Si lo dejamos en blanco, traerá todas las noticias publicadas.

Se agregaron los botones de login/register y si estamos logueados el de Perfil/logout y un boton que te lleva a todas las noticias publicadas.

La pagina funciona de forma responsiva, y permite se carguen imagenes.
