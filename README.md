# Club Atlético Juventud de Liniers
Proyecto Final del Instituto Superior Nuestra Señora de la Paz, ubicado en Buenos Aires, Argentina.

El mismo fue realizado para el Club deportivo Juventud de Liniers, ubicado en Montiel 1174, CABA. 

El mismo consta de un software de gestion de socios, con carga de de los mismos, y la generación básica de comprobantes de pago correspondientes a los socios, con gestion de pagos en el mismo.

## Librerias utilizadas en el proyecto.
1. Django para el framework base.
2. Django-Jazzmin para la gestión administrativa de la propia app (backoffice).
3. Crispy-bootstrap5 para la gestión de formularios del sistema.



## Como instalar el proyecto de manera local.
Primeramente tener descargado Python de la página oficial: www.python.org

Luego crear el entorno correspondiente, utilizando el comando pip vía CMD (Símbolo del Sistema).
```
python -m venv CAJL
```
Luego instalar las librerias utilizadas en el proyecto arriba, usando el comando pip
```
pip install django
```
```
pip install django-jazzmin
```
```
pip install crispy-bootstrap5
```
```
pip install django-bootstrap-datepicker-plus
```
Navegar hacia la carpeta donde esta ubicado el manage.py y tirar el comando runserver:
```
py manage.py runserver
```
