# proyecto-django

Para acceder a la funcionalidad deben instalar los requerimientos que se detallan en requeriments.txt y luego hacer:

python manage.py migrate
python manage.py runserver

*Una vez iniciada la pagina:

Acceder en el navegador a la direccion http://127.0.0.1:8000/inicio/

*Una vez cargada la pagina se encontrara con 4 botones superiores, estos son:
"Inicio" siempre lo llevara a la pantalla principal.

"Buscar un vehiculo" esto lo lleva al listado completo de vehiculos, el cual posee en la parte superior 3 cuadros de busqueda por Marca, Modelo y Año. Puede buscar por el filtro que necesite, no es necesario rellenar los 3 filtros para realizar la busqueda. Una vez puesto un filtro apareceran los vehiculos que pertenezcan a dicha busqueda y aparecera un boton de "limpiar busqueda" para restablecer el listado. La clase Vehiculo se encuentra en /inicio/models.py y su vista en /inicio/views.py.

"Registrarse" genera un formulario para crear un usuario y lo guarda en la BD. El formulario se encuentra en /usuarios/forms.py y su vista en /usuarios/views.py.

"Login" genera una vista para introducir el usuario y la clave y lo busca en la BD, lo verifica e inicia la sesion. La vista en /usuarios/views.py.

*Y en la parte inferior de la pagina esta el boton:
"About" este boton muestra un breve mensaje del creador de la pagina.

*Luego de iniciar la sesion aparecen distintos botones nuevos:

"Agregar queja" sirve para que un usuario pueda en un recuadro de texto describir su problema y este se guarde en la BD. La clase Queja se encuentra en /inicio/models.py y su vista en /inicio/views.py.

"Lista quejas" sirve para que los usuarios puedan ver el listado de quejas y su fecha de creacion. La vista de la lista de quejas se encuentra en /inicio/views.py.

"Editar Perfil" este boton en la parte superior sirve para que un usuario pueda introducir su nombre y apellido, y ademas cargar su imagen o avatar el cual se visualizara en la parte superior. La clase para la edicion se llama InfoExtra y se encuentra en /usuarios/forms.py y su vista en /usuarios/views.py.

** Usuario Administrador **

El administrador cuenta con todos los botones detallos pero ademas tiene los botones de:
"Agregar Vehiculo" para crear nuevos vehiculos poniendo su Marca, Modelo y Año. La clase Vehiculo se encuentra en /inicio/models.py y su vista en /inicio/views.py.

Y luego al ir al listado de vehiculo el administrador puede Eliminar un vehiculo dando click sobre "Eliminar" que aparecera junto a un vehiculo, o tambien puede dar en el boton "Editar" para cambiar la Marca, el Modelo o Año del mismo.