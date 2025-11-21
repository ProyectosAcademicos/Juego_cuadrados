# 🎮 Juego Cuadros  
Proyecto desarrollado en Python utilizando **Pygame**. Este repositorio contiene el código fuente de un videojuego simple donde se aplican principios de programación orientada a objetos, físicas básicas y manejo de eventos.

Este README tiene como objetivo entregar instrucciones claras para que cualquier colaborador pueda instalar, ejecutar y continuar el desarrollo del proyecto en su propio computador.

---

## 📌 Características del Proyecto
- Desarrollado con **Python 3.9+**
- Utiliza la librería **Pygame 2.6.1**
- Estructura modular (archivos separados por funcionalidades)
- Compatible con macOS, Windows y Linux
- Preparado para ser ejecutado dentro de un **entorno virtual (venv)**

---

# 🚀 Instalación y Configuración

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/ProyectosAcademicos/Levelup-store-react.git
```

⚠️ Si el repositorio del juego es distinto, reemplazar el link anterior por el correcto.
Luego ingresar al directorio del proyecto:

```bash
cd Juego_cuadros/Juego_cuadrados/código
```

2️⃣ Crear un entorno virtual (recomendado)

```bash
python3 -m venv .venv
```
Activar el entorno virtual:
macOS / Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.\venv\Scripts\activate
```

Debes ver algo así en tu terminal:

```bash
(.venv)
```

3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

Si el archivo requirements.txt aún no existe, instalar manualmente:

```bash
pip install pygame
```

Y luego generar el archivo:

```bash
pip freeze > requirements.txt
```

▶️ Ejecutar el Juego
Con el entorno virtual activado:

```bash
python bala_juego.py
```

o el archivo principal que corresponda, por ejemplo:

```bash
python main.py
```

Estructura del proyecto:

```bash
📁 código/
 ├── bala_juego.py          # Archivo principal o módulo del juego
 ├── jugador.py             # Control del personaje
 ├── enemigos.py            # Lógica de enemigos
 ├── niveles.py             # Configuración de niveles
 ├── assets/                # Imágenes, sonidos, sprites
 ├── utils/                 # Funciones auxiliares
 ├── .venv/                 # Entorno virtual (no se sube a GitHub)
 ├── requirements.txt       # Dependencias
 └── README.md              # Documentación del proyecto

```

👨‍💻 Guía para Desarrolladores
➤ Crear una rama personal
Cada colaborador debe trabajar en su propia rama:

```bash
git checkout -b develop_tuNombre
```

```bash
git add .
git commit -m "Descripción del cambio"
git push origin develop_tuNombre
```

🔧 Solución de problemas comunes
❗ Error: ModuleNotFoundError: No module named 'pygame'
Solución:
Activar entorno virtual:

```bash
source .venv/bin/activate
```

Instalar pygame:

```bash
pip install pygame
``

















