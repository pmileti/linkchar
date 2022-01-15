# Desafio backend por Pablo Mileti

### Jueves 13 de enero de 2022 - (día 1/2)

Se trabaja sobre la rama master en el incio de la base del proyecto sin la API
- Preparación del virtualenv
- Activación del virtual env
- Se instalan:
  - django
  - djangorestframework
  - markdown
  - celery
- Con pip freeze se genera el archivo requirements.txt
- Se inicia el proyecto llamado "desafio"
- Se migran las bases de datos
- Se crea un superuser para el acceso desde admin
  usuario:linkchar /   clave: mileti
- Se toca settings.py para idiomas 'es'
- Se desarrolla acceso via /admin/ y /api-test/ para confirmar que todo está operativo
- Instalo git y lo configuro para poder subir al repositorio la base del proyecto
- Se pushea sobre master la base

### Viernes 14 de enero de 2022 - (día 2/2)

- Se crea la app 'apis' y se la registra en settings.py
- Se crea el modelo en función del json que se debe volcar a la base de datos
- Se migra el nuevo modelo y se lo registra para hacerlo administrable
- Se crean los serializadores del modelo
- Se crean las urls de los endpoints solicitados
- Se instala request y se actualiza requirements.txt
- Se crean las vistas con los endpoints funcionando
- Se incorpora celery con su task y RabbitMQ como worker
- Se reimplementa el endpoint para ser asincrono
- Este es el comando de Celery: 
```
celery -A desafio worker -l info
```
- Asi se testean los endpoints desde httpie:
```
http POST http://127.0.0.1:8000/populate-apis

http POST http://127.0.0.1:8000/keyword keyword="a"

http POST http://127.0.0.1:8000/category category="Animals"

http POST http://127.0.0.1:8000/ordered-list

http POST http://127.0.0.1:8000/item pk="1419"

```
- Se pushea sobre rama apis
- Me peleo con el _pycache_ y el git
- Se mergea al master
- Se hace publico el repositorio
