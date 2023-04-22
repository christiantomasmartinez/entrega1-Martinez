# proyecto-django

Para acceder a la funcionalidad debe hacer:

-pip install django
python manage.py migrate
python manage.py runserver

Luego:

acceder en el navegador a la direccion http://127.0.0.1:8000/inicio/
una vez cargada la pagina se encontrara con 5 botones
"Inicio" siempre lo llevara a la pantalla principal
"Registrar comprador" genera una instancia de la clase Comprador y lo guarda en la BD. La clase se encuentra en models.py y su vista en views.py
"Registrar vendedor" genera una instancia de la clase Vendedor y lo guarda en la BD. La clase se encuentra en models.py y su vista en views.py
"Agregar vehiculo" genera una instancia de la clase Vehiculo y lo guarda en la BD. La clase se encuentra en models.py y su vista en views.py
"Buscar un vehiculo" busca en la BD el modelo de vehiculo solicitado. Esto esta en la view lista_vehiculos con su template lista_vehiculos.html
Cada boton de registrar tiene su respuesta de registro exitoso. 