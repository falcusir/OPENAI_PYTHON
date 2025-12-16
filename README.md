# 📌 Proyecto: Consumo de la API de OpenAI con Python

Este proyecto demuestra cómo integrar la **API de OpenAI** en un proyecto desarrollado con **Python**, aplicando buenas prácticas como el uso de entornos virtuales, variables de entorno y control de versiones con Git.

---
## 🧩 Requisitos previos

Antes de ejecutar el proyecto, tener lo siguiente:

- Python 3.9 o superior
- Visual Studio Code
- Cuenta activa en OpenAI (Plataforma API)
- Git instalado (opcional)

Para verificar la versión de Python, ejecute:

```
python --version
```
---
## ⚙️ Instalación

### Paso 1️⃣ Abrir el proyecto

1. Crear una carpeta llamada `OPENAI_PYTHON`.
2. Abrir Visual Studio Code.
3. Seleccionar **Archivo → Abrir carpeta** y elegir la carpeta del proyecto.


### Paso 2️⃣ Crear el entorno virtual

Desde la terminal integrada de Visual Studio Code, ejecutar:

```bash
python -m venv venv
```


### Paso 3️⃣ Activar el entorno virtual (Windows)

```bash
venv\Scripts\activate.bat
```
Si el entorno está activo, la terminal mostrará **(venv)** al inicio.


### Paso 4️⃣ Instalar dependencias

Con el entorno virtual activo, ejecutar:

```bash
pip install openai python-dotenv
```


### Paso 5️⃣ Configurar variables de entorno

Crear un archivo **.env** en la raíz del proyecto y agregar:

```
- OPENAI_API_KEY= api_key_aqui
- OPENAI_ORG_ID= organization_id_aqui
```


### Paso 6️⃣ Configurar el archivo .gitignore

Crear o editar el archivo **.gitignore** y agregar:

```
.env
venv/
__pycache__/
```


### Paso 7️⃣ Crear el archivo principal

Crear el archivo **main.py** y escribir el código encargado de:

- Cargar las variables de entorno
- Conectarse a la API de OpenAI
- Enviar un prompt
- Mostrar la respuesta en la terminal

---
## ▶️ Ejecución

Con el entorno virtual activo, ejecutar el programa con el comando:

```bash
python main.py
```
_Si la configuración es correcta, se mostrará en la terminal una respuesta generada por el modelo de inteligencia artificial._

---
## 🧪 Pruebas

Para realizar pruebas adicionales:

1. Modificar el texto del prompt en el archivo **main.py**
2. Guardar los cambios
3. Ejecutar nuevamente:

```bash
python main.py
```
_Cada cambio en el prompt generará una respuesta diferente._

---
## 🔐 Buenas prácticas aplicadas

- Uso de entorno virtual para aislar dependencias
- Protección de la API Key con variables de entorno
- Uso del archivo **.gitignore**
- Código organizado y legible
- Manejo de errores en Python