# weather-app

Aplicación de predicción del clima en ciudades y paises.

Se crean dos modeles:

- City:
- 
        - Id
        - Name
        - Flag

- Country:
- 
        - ID
        - Iso_code
        - Flag


Las herramientas que se utilizaron en el desarrollo fueron:

 - Python como lenguaje de programación.
 - Django.
 - librerias: djangorestframework~=3.14 - drf-yasg~=1.21.
 - redoc y swagger.


link de redoc: http://localhost:8000/redoc/#tag/countries/operation/countries_update
link de swagger: http://localhost:8000/swagger/
        

para instalar los requerimientos de librerias utilice el siguiente comando: pip install -r .\requirements.txt

Para entrar al admin de django:
User: csuaza
password: 1234

Nota: Si tiene probelma para ingresar al admin puede crear un nuevo super usuario con el comando python manage.py createsuperuser


para correr la palicación utilice el comando: python manage.py runserver


Nota: La presente apliciación continua en desarrollo pero, con lo hecho hasta el momento se cumple con los requicitos del rete practico.



