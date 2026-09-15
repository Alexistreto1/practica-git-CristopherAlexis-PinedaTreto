## 1. **Cristopher Alexis Pineda Treto**
## 2. **263007**
## 3. **Creación y sincronización de un repositorio local con Git y GitHub utilizando PowerShell**
## 4. Objetivo 
Aprender a utilizar comandos básicos de PowerShell para crear y administrar carpetas, así como utilizar Git para crear un repositorio local, controlar versiones y sincronizarlo con un repositorio remoto en GitHub.
## 5. Descripción 
Primero se abrió PowerShell y se utilizó para ubicarse en el escritorio y crear la carpeta destinada a la práctica. Posteriormente se ingresó a la carpeta creada y se configuró Git con el nombre y correo electrónico del usuario.
Después se inicializó el repositorio local utilizando `git init`. Se crearon y agregaron los archivos necesarios para la práctica y se verificó el estado del repositorio mediante `git status`.
Los archivos fueron agregados al área de preparación mediante `git add` y posteriormente se creó un commit para guardar los cambios.
Finalmente, se creó un repositorio en GitHub y se vinculó con el repositorio local utilizando `git remote add origin`. Después se utilizó `git push` para sincronizar el repositorio local con GitHub y `git pull` para obtener cambios desde GitHub hacia el repositorio local.

## 6. Comandos de Git 
### Comandos 
```text
git config --global user.name "Nombre"
git config --global user.email "correo"
git init
git status
git add README.md datos.txt
git commit -m "Primer commit"
git remote add origin URL_DEL_REPOSITORIO
git branch -M main
git push -u origin main
git pull origin main
```
## 7. Explicación de la función

* **git config --global user.name:** establece el nombre del usuario para Git.
* **git config --global user.email:** establece el correo electrónico del usuario para Git.
* **git init:** inicializa un repositorio local de Git dentro de la carpeta actual.
* **git status:** muestra el estado del repositorio y los archivos que tienen cambios.
* **git add:** agrega archivos al área de preparación para el siguiente commit.
* **git commit:** guarda los cambios preparados en el historial de Git.
* **git remote add origin:** establece la conexión entre el repositorio local y el repositorio remoto de GitHub.
* **git branch -M main:** establece `main` como nombre de la rama principal.
* **git push:** envía los cambios del repositorio local hacia GitHub.
* **git pull:** obtiene los cambios del repositorio de GitHub y los integra en el repositorio local.
## 8. Explicación de cómo se creó el repositorio local
Primero se utilizó PowerShell para crear la carpeta de trabajo mediante:
```text
mkdir practica-git-CristopherAlexis-PinedaTreto
```
Después se ingresó a ella con:
```text
cd practica-git-CristopherAlexis-PinedaTreto
```
Una vez dentro de la carpeta se utilizó:
```text
git init
```
Este comando creó el repositorio local de Git y permitió comenzar a llevar un control de versiones de los archivos de la práctica.

## 9. Explicación de cómo se vinculó el repositorio local con GitHub
Después de crear el repositorio en GitHub, se utilizó el comando:

```text
git remote add origin URL_DEL_REPOSITORIO
```
Esto estableció la conexión entre el repositorio local y el repositorio remoto de GitHub.
También se estableció la rama principal mediante:
```text
git branch -M main
```
## 10. Explicación de la sincronización Local → GitHub
Para enviar los cambios realizados en el equipo hacia GitHub se utilizó:
```text
git push -u origin main
```
Este comando envía los commits de la rama `main` del repositorio local al repositorio remoto de GitHub.

## 11. Explicación de la sincronización GitHub → Local
Para obtener cambios realizados en el repositorio remoto se utiliza:

```text
git pull origin main
```
Este comando descarga los cambios de GitHub y los integra en el repositorio local.

## 12. Descripción de los archivos contenidos en el repositorio
El repositorio contiene los archivos utilizados durante la práctica:
* **README.md:** contiene información, instrucciones y documentación relacionada con la práctica.
* **datos.txt:** contiene los datos utilizados como parte de la práctica y permite comprobar el funcionamiento del control de versiones.

## Conclusión personal
Con esta práctica aprendí a utilizar Git para controlar los cambios realizados en los archivos de un proyecto y a sincronizar un repositorio local con GitHub.
También comprendí la función de los comandos principales, como `git init`, `git add`, `git commit`, `git push` y `git pull`.
La práctica me permitió comprobar que los cambios pueden realizarse tanto desde la computadora como desde GitHub, y que es importante mantener ambos repositorios sincronizados.
Además, aprendí a utilizar comandos de PowerShell para crear carpetas, navegar entre directorios y trabajar desde la terminal.
