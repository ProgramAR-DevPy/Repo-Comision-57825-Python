# COMANDOS UTILIZADOS EN EL AFTER
- Configuración inicial:

*git config --global user.name "Tu Nombre":* Reemplaza "Tu Nombre" con tu nombre completo.
*git config --global user.email "tucorreo@ejemplo.com":* Reemplaza con tu dirección de correo electrónico.

- Guardar cambios:

1. *git add \<archivo>:* Agrega un archivo específico al área de preparación (staging area).
2. *git add .:* Agrega todos los archivos modificados al área de preparación.
3. *git commit -m "Mensaje descriptivo":* Crea un commit con los cambios preparados, incluyendo un mensaje que describa los cambios.

### ¡Importante!
1. Clonar un repositorio existente: Si quieres trabajar en un proyecto existente, usa git clone \<url-del-repositorio>.
2. Ver el estado del repositorio: Usa git status para ver qué archivos han sido modificados, agregados o eliminados.



# OTROS COMANDOS Y PROCEDIMIENTOS NO VISTA EN EL AFTER (TRANQUILOS LOS VAMOS A VER EN CLASE)
#### VISTO EN EL AFTER
- Configuración inicial:

1. *git config --global user.name "Tu Nombre":* Reemplaza "Tu Nombre" con tu nombre completo.
1. *git config --global user.email "tucorreo@ejemplo.com":* Reemplaza con tu dirección de correo electrónico.
Estos comandos configuran tu nombre y correo electrónico, que se asociarán a tus commits.

### NO VISTO EN EL AFTER
- Crear un nuevo repositorio:

1. *git init:* Este comando crea un nuevo repositorio Git en el directorio actual.

### VISTO EN EL AFTER
- Guardar cambios:

1. *git add <archivo>:* Agrega un archivo específico al área de preparación (staging area).
2. *git add .:* Agrega todos los archivos modificados al área de preparación.
3. *git commit -m "Mensaje descriptivo":* Crea un commit con los cambios preparados, incluyendo un mensaje que describa los cambios.


### NO VISTO EN EL AFTER
Conectar con un repositorio remoto (opcional):
- ***Nota: Si creamos el repo local con git init, y trabajamos de forma local. Y queremos tener ese repo local en remoto. Creamos en github un repo remoto. Y lo conectamos con nuestro repositorio local usando el siguiente comando:***


1. *git remote add origin \<url-del-repositorio>:* Asocia tu repositorio local con uno remoto (como GitHub o Bitbucket).
2. *git push -u origin main:* Sube tus commits al repositorio remoto (la primera vez necesitas la opción -u). Luego se hacen los commit de forma normal. 