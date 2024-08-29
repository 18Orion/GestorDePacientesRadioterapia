# **Gestor de pacientes**
Este programa y sus herramientas tienen como objetivo la gestión de los pacientes de radiofísica.
Al tener un front-end desarrollado en QT y escrito en python el programa es eficiente y fácil de usar.
## **¿Por qué usarlo?**
El objetivo de este programa es sustituir herramientas previas como excel y dar una respuesta a la baja utilidad de los caros programas de uso de registro de pacientes. Al guardar los pacientes en una base de datos MySQL, aumentamos la seguridad imponiendo un sistema de usuarios.
Además los datos del paciente y del tratamiento se almacenan aparte dandole una capa extra de anonimato a los datos, que solo se relacionan por su NUSHA.
## **Herramientas incluidas**
El programa consta de dos herramientas principales: el mecanizado de pacientes y la actividad de explotación de datos.
En la primera encontramos todos los datos a rellenar de un paciente tomando el tipo de tratamiento, el número de cálculo, diferentes fechas y las observaciones de los especialistas.
En la segunda encontramos una serie de filtros para encontrar los datos que se necesiten y exportarlos a un excel con el objetivo de usarlos.
Ambas herramientas se han desarrollado con el error humano en mente de tal forma que evitan errores de mecanizado en la medida de lo posible.
## **Uso**
Al desempaquetar encontramos un archivo suite.py o su equivalente compilado en el caso de descragar los paquetes para Windows o Linux. Al ejecutarlo accedemos al login y después al launcher.
Antes de compilarlo o ejecutarlo hay que descargar los requisitos que se especifican en requirements.txt con:
```
pip install -r requirements.txt --break-system-packages
```
Para compilar se usa ```
make all
```.
Para ejecutarlo se usa ```
python suite.py
```
## **Scripts**
Este programa viene con varios scripts con el objetivo de migrar o simular las diferentes bases de datos para comprobar su funcionamiento. Estos se encuentran bajo la carpeta scripts y es importExcel.py y createDummyDB.py. Estas funcionan con el estándar de conexión que proporciona la libreria MySQLdb.py. Además necesita la configuración de configuration.json por lo que tanto la carpeta libs y el configuration.json deben ser copiados antes de usar los scripts.