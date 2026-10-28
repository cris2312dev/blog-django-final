# DevBlog - Proyecto Consolidado Blog Web en Django

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Plataforma de blog web desarrollada con **Python** y **Django**, estructurada bajo la arquitectura MVT (Model-View-Template). Permite la gestión completa de publicaciones (CRUD), carga dinámica de imágenes multimedia, sistema de cuentas con autenticación y perfiles de usuario, rutas protegidas y motor de búsqueda interactivo.

---

## 📌 Funcionalidades Principales

### 📰 Publicaciones & CRUD
- **Listado y paginación** de artículos desde la interfaz web pública.
- **Detalle completo** de publicaciones con formato de lectura estilizado.
- **Creación, Edición y Eliminación** de posts desde formularios web amigables.
- **Manejo seguro de imágenes**: integración con `Pillow` y configuración de `MEDIA_URL` / `MEDIA_ROOT`. La plantilla incluye fallback dinámico en caso de que un artículo no cuente con imagen de portada.

### 👤 Autenticación & Usuarios
- **Registro** de nuevos usuarios con validación de credenciales.
- **Inicio y Cierre de Sesión** con redirecciones y alertas visuales.
- **Diferenciación de roles**: los visitantes anónimos pueden explorar artículos, mientras que la publicación y edición requiere inicio de sesión.
- **Perfil de usuario editable**: avatar personalizado, biografía, enlace a sitio web y listado de posts publicados por cada autor.

### 🔒 Rutas Protegidas y Permisos
- Protección estricta en backend mediante `LoginRequiredMixin` y decoradores `@login_required` (evita acceso directo por URL).
- Verificación de autoría (`UserPassesTestMixin`): solo el autor de una publicación o un superusuario puede editarla o eliminarla.

### 🔍 Motor de Búsqueda
- Búsqueda en tiempo real por título, subtítulo o contenido textual.
- Notificación y vista amigable cuando la búsqueda no arroja coincidencias.

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.10+
- **Framework Web:** Django 5
- **Procesamiento de Imágenes:** Pillow
- **Variables de Entorno:** python-decouple
- **Base de Datos:** SQLite (para desarrollo y testing local)
- **Frontend & Estilos:** Bootstrap 5, Bootstrap Icons, CSS3 responsivo

---

## 🚀 Guía de Instalación y Ejecución Local

Sigue estos sencillos pasos para clonar, configurar e iniciar el proyecto en tu entorno local:

### 1. Clonar el repositorio
```bash
git clone <URL_DE_TU_REPOSITORIO_GITHUB>
cd blog-django-final
```

### 2. Crear y activar el entorno virtual

- **En Windows:**
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```

- **En Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno
Copia el archivo de plantilla `.env.example` para generar tu `.env` local:
```bash
# En Windows (PowerShell):
Copy-Item .env.example .env

# En Linux / macOS:
cp .env.example .env
```
*(El archivo `.env` ya viene preconfigurado para pruebas locales en desarrollo).*

### 5. Aplicar migraciones a la base de datos
```bash
python manage.py migrate
```

### 6. Poblar datos iniciales o crear un superusuario

- **Opción A (Recomendada): Poblar datos de prueba automáticos**
  ```bash
  python seed_data.py
  ```
  Esto generará:
  - **Superusuario (Admin):** usuario `admin` | contraseña `AdminPass123!`
  - **Usuario Estándar:** usuario `developer` | contraseña `DevPass123!`
  - Tres artículos completos de demostración.

- **Opción B: Crear superusuario manualmente para el panel admin**
  ```bash
  python manage.py createsuperuser
  ```

### 7. Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```

Abre tu navegador e ingresa a: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

Para ingresar al panel de administración de Django: **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**

---

## 🧪 Ejecutar Pruebas Automatizadas

El proyecto incluye tests unitarios y de integración para validar la seguridad de las rutas, el CRUD y el motor de búsqueda:

```bash
python manage.py test blog
```

---

## 📁 Estructura del Proyecto

```text
blog-django-final/
├── accounts/               # Aplicación de autenticación y perfiles
│   ├── migrations/         # Migraciones de base de datos
│   ├── forms.py            # Formularios de registro y edición de perfil
│   ├── models.py           # Modelo Profile 1 a 1 con User
│   ├── urls.py             # Rutas de autenticación
│   └── views.py            # Vistas basadas en funciones y clases
├── blog/                   # Aplicación principal del blog
│   ├── migrations/         # Migraciones de publicaciones
│   ├── forms.py            # Formulario para posts
│   ├── models.py           # Modelo Post con carga de imagen
│   ├── tests.py            # Pruebas automatizadas del sistema
│   ├── urls.py             # Enrutamiento de posts y vistas públicas
│   └── views.py            # CRUD completo con CBVs (ListView, DetailView, etc.)
├── blog_project/           # Configuración central del proyecto Django
│   ├── settings.py         # Configuración desacoplada con python-decouple
│   ├── urls.py             # Rutas globales y manejo de media
│   └── wsgi.py
├── static/                 # Archivos estáticos globales (CSS personalizados)
├── templates/              # Plantillas HTML con Bootstrap 5
│   ├── base.html           # Layout principal heredable
│   ├── accounts/           # Plantillas de login, registro y perfil
│   └── blog/               # Plantillas de listado, detalle y formularios CRUD
├── .env.example            # Plantilla para variables de entorno seguras
├── .gitignore              # Exclusiones de Git (venv, .env, db.sqlite3, media)
├── manage.py
├── requirements.txt        # Dependencias fijadas del proyecto
├── seed_data.py            # Script auxiliar para inicializar datos
└── README.md               # Documentación general del repositorio
```

---

## 👨‍💻 Autor

- **Carlos Bocangel**
- Proyecto desarrollado como Entrega Final del recorrido de Python & Django.
