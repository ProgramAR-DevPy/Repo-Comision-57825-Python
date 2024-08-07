# Git: ¡Tu Máquina del Tiempo para el Código! ⏰

- Imagina que estás escribiendo una novela 📖. A medida que avanzas, haces cambios, agregas capítulos, corriges errores... ¿Y si pudieras guardar instantáneas de tu novela en diferentes momentos, para poder volver atrás si te equivocas o quieres comparar versiones? ¡Eso es lo que hace Git!.

# SOY UN CRACK



- Git es un sistema de control de versiones (VCS) que te permite llevar un registro de los cambios en tus archivos a lo largo del tiempo. Es como tener una máquina del tiempo para tu código, ¡puedes viajar al pasado y restaurar versiones anteriores si es necesario! 🕰️

### Los 3 Estados de Git: ¡El Flujo de Trabajo! 🌊
1. **Working Directory (Directorio de Trabajo):** Es donde creas y modificas tus archivos. Es como el borrador de tu novela, donde puedes experimentar y hacer cambios libremente.

2. **Staging Area (Área de Preparación):** Es donde seleccionas los cambios que quieres incluir en la próxima instantánea (commit). Es como elegir qué capítulos de tu novela quieres publicar en la próxima edición.

3. **Repository (Repositorio):** Es donde se almacenan las instantáneas (commits) de tu proyecto. Es como la biblioteca donde guardas todas las ediciones de tu novela.

### Git y GitHub: ¡La Pareja Perfecta! 👫
Git es el sistema de control de versiones que se ejecuta en tu computadora. GitHub es una plataforma en línea que te permite almacenar y compartir tus repositorios Git. Es como tener una copia de seguridad de tu novela en la nube, ¡accesible desde cualquier lugar! ☁️

### Configurando Git por Primera Vez: ¡Preséntate! 👤
Antes de empezar a usar Git, debes decirle quién eres:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_email@example.com"
```

#### ¡Esto es importante para que Git pueda identificar quién hizo cada cambio en el proyecto!

### Comandos Básicos de Git: ¡Empieza a Viajar en el Tiempo! ⏰
- **git init:** Crea un nuevo repositorio Git en tu proyecto.
- **git add:** Agrega archivos al área de preparación (staging area).
- **git commit:** Crea una instantánea (commit) de los cambios en el área de preparación.
- **git status:** Muestra el estado de los archivos en tu repositorio.
- **git log:** Muestra el historial de commits.


### **HINT: Para pensar.**

### Para Pensar: ¿Cuál es la Diferencia Principal entre Git y GitHub? 🤔

.....................................



# Creando Repositorios Git: ¡Tu Proyecto Bajo Control! 📦
- Imagina que estás construyendo un rompecabezas gigante 🧩. Para mantener las piezas organizadas y evitar perderlas, las guardas en una caja especial. ¡Un repositorio Git es como esa caja para tu proyecto de código!

- Un repositorio Git es un espacio donde almacenas y gestionas el historial de cambios de tu proyecto. Es como una máquina del tiempo para tu código, ¡puedes volver a versiones anteriores si es necesario!

### Git Init: ¡Crea tu Caja de Herramientas! 🧰
El comando git init crea un nuevo repositorio Git en la carpeta actual. Es como preparar la caja para guardar tus piezas de rompecabezas.

```bash
git init mi_repositorio
```

1. Este comando crea una carpeta oculta llamada .git dentro de mi_repositorio. Esta carpeta es donde Git almacena toda la información sobre el historial de tu proyecto.

### Git Status: ¡Revisa el Estado de tu Proyecto! 👀
2. El comando git status te muestra el estado actual de tu repositorio. Es como mirar dentro de la caja para ver qué piezas están sueltas y cuáles ya están organizadas.

```bash
git status
```

#### Te mostrará:

- **Untracked files:** Archivos nuevos que Git aún no está rastreando.
- **Changes not staged for commit:** Cambios en archivos que Git está rastreando, pero que aún no has preparado para incluir en la próxima instantánea (commit).
- **Changes to be committed:** Cambios que has preparado para incluir en el próximo commit.

### Git Add: ¡Prepara las Piezas para Guardar! 🧩
3. El comando git add agrega los archivos que especificas al área de preparación (staging area). Es como seleccionar las piezas del rompecabezas que quieres guardar en la caja.

```bash
git add index.html
```

#### También puedes usar git add . para agregar todos los archivos nuevos y modificados.

### Git Commit: ¡Toma una Instantánea! 📸
3. El comando git commit crea una nueva instantánea (commit) de los cambios que has preparado en el área de preparación. Es como tomar una foto de tu rompecabezas en un momento determinado, para poder volver a ese estado más tarde si lo necesitas.

```bash
git commit -m "Primer archivo del repositorio"
```

- **-m:** El mensaje (-m) es una breve descripción de los cambios que estás guardando.

### Git Log: ¡Revisa tu Historial de Cambios! 📖
4. El comando git log te muestra el historial de commits de tu repositorio. Es como hojear un álbum de fotos de tu rompecabezas, viendo cómo ha evolucionado a lo largo del tiempo.

```bash
git log
```

# Ramas en Git: ¡Organiza tus Cambios y Experimenta sin Miedo! 🌳
- Imagina que estás escribiendo una novela 📖. ¿Quieres probar un final alternativo? ¿O quizás agregar un nuevo personaje sin afectar la historia principal? ¡Las ramas en Git te permiten hacer eso y mucho más!

- Una rama es como una línea de tiempo paralela en tu proyecto. Puedes crear una rama para trabajar en nuevas características, corregir errores o experimentar con ideas, sin afectar la rama principal (generalmente llamada master o main).

### Git Branch: ¡Crea y Explora Nuevas Posibilidades! 🌿
- 1. **git branch nombre_rama:** Crea una nueva rama con el nombre que le indiques.
- 2. **git branch:** Muestra una lista de todas las ramas existentes, con un asterisco (*) marcando la rama actual.
- 3. **git branch -l:** Muestra una lista más detallada de las ramas, incluyendo sus nombres completos y referencias.

### Git Checkout: ¡Viaja entre Ramas! 🚂

- **git checkout nombre_rama:** Cambia a la rama especificada.
- **git checkout -b nombre_rama:** Crea una nueva rama y cambia a ella automáticamente.

### Git Merge: ¡Une tus Ramas como un Río! 🌊
**git merge nombre_rama:** Fusiona los cambios de la rama especificada en la rama actual.

### Git Branch -D: ¡Elimina Ramas que ya no Necesitas! ✂️
**git branch -D nombre_rama:** Elimina la rama especificada (solo si ya has fusionado sus cambios).

### Ejemplo: ¡Creando y Fusionando Ramas! 🌳🔀
- Crear una rama: git branch nueva_rama
- Cambiar a la rama: git checkout nueva_rama
- Hacer cambios en los archivos.
- Agregar los cambios al área de preparación: git add .
- Crear un commit: git commit -m "Mensaje descriptivo"
- Volver a la rama principal: git checkout master
- Fusionar los cambios: git merge nueva_rama

### Git Checkout: ¡Viaja en el Tiempo a un Commit Específico! ⏰
Puedes usar git checkout para volver a un commit anterior, pero ten en cuenta que esto te llevará a un estado "detached HEAD" (cabeza separada), donde tus cambios no estarán asociados a ninguna rama.

```bash
git checkout <hash_del_commit>  # Reemplaza <hash_del_commit> por el código del commit
```
### ¡Ramas para un Desarrollo Organizado! 🌳
- Las ramas son una herramienta esencial para trabajar en equipo y mantener tu proyecto organizado. ¡Úsalas para experimentar, colaborar y mantener tu código limpio y ordenado!