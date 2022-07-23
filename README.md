
# Psico

## Integrantes
### Andrés Felipe Nausan Fajardo
### Sebastian Felipe Martinez Samaca
### Gloria Patricia Duran Benavides
### Wilson Arbey Delgado Manzo
### Michael Steven Mogollon Leon

## Migracion de BitBucket a GitHub

Antiguo repositorio **https://bitbucket.org/wilsonarbeydelgado/psico/src/master/**. 

Se realizo la migracion para automatizar los despliegues en Heroku y facilitar el desarrollo del proyecto
# Como instalar el proyecto.

# 1. Clonar el repositorio 

Ejecutar el comando ```git clone "URL repositorio"```

# 2. Creacion Entorno Virtual y Archivo .env

Ejecutar el comando ```python -m venv env``` en la carpeta raiz del proyecto

# 3. Activacion del Entorno Virtual

Abrir terminal en la ruta del proyecto y ejecutar:

Para windows:

```env\Scripts\activate```

Para linux: 

```source env/bin/activate```

# 4. Instalacion de Librerias (Archivo requirements)

```pip install -r requirements.txt```

# 5. Ejecutar el Proeycto

```python manage.py runserver```

# 6. FIN

# Introduccion
El mundo distópico que narra George Orwell en 1984 no está lejos de la realidad de cientos de personas, que fervientemente creen y apropian las realidades creadas y transmitidas por una pantalla, dentro de las diferentes consecuencias de vivir en este mundo surge la situación de que, a mayor conexión y comunicación, las expectativas y estándares afectan de manera negativa la salud mental: “De acuerdo con la Organización Mundial de la Salud – OMS, en el mundo hay alrededor de mil millones de personas que viven con un trastorno mental, en donde la depresión es una de las principales causas de enfermedades y discapacidad en los niños, niñas y adolescentes, así como la OMS ha resaltado que aproximadamente cada 40 segundos en el mundo alguien muere por suicidio” DANE (2021). Por otro lado, el acceso a servicios de salud mental de calidad es escaso, según las Naciones Unidas “en países de ingresos bajos y medios, un poco más del 75% de personas con problemas de salud mental no reciben ningún tipo de tratamiento”, esto también recae en la brecha de información entre los usuarios y los profesionales de la salud mental.
En este sentido Psico acerca la oferta a la demanda de servicios de salud mental, permitiendo que la comunidad tenga información concisa y rápida de diferentes tipos de especialistas, su localización, medios de contacto y un ranking de precios de los servicios, acompañado de una sección de calificaciones con los comentarios de otros usuarios, permitiendo así aportar con la información necesaria para una adecuada elección del profesional de la salud, según los intereses y necesidades de los usuarios.
Alcance del proyecto
Construir una herramienta de software web que resuelva la necesidad de obtener un servicio psicológico. Este sistema debe ser capaz de mostrar la información clara para que cualquier cliente potencial pueda contactar con el profesional que le interese en esta área. Para lo cual es necesario crear la base de datos con los niveles de seguridad apropiados para que cada profesional deposite su información de contacto, credenciales, entre otros.

