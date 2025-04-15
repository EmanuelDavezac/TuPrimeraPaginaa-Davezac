# VideoGameManager

**VideoGameManager** es una aplicación web desarrollada con Django que permite gestionar una base de datos de videojuegos, desarrolladores y plataformas de manera intuitiva.

# Funcionalidades principales

- Agregar nuevos videojuegos con sus respectivos datos.
- Registrar desarrolladores y plataformas.
- Buscar videojuegos en la base de datos.
- Interfaz web simple y amigable utilizando HTML y Django Templates.

# Estructura del Proyecto

- `VideoGameManager/` – Configuración general del proyecto Django.
- `videojuegos_app/` – Aplicación principal con toda la lógica de la app:
  - `models.py` – Modelos para videojuegos, desarrolladores y plataformas.
  - `views.py` – Vistas para manejar las operaciones.
  - `forms.py` – Formularios para el ingreso de datos.
  - `templates/` – Archivos HTML para la interfaz de usuario.

# Tecnologías utilizadas

- Python 3.13.1
- Django
- HTML
- SQLite
