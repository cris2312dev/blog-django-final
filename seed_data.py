import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Post
from accounts.models import Profile

# 1. Crear Superusuario / Admin si no existe
admin_user, created = User.objects.get_or_create(
    username='admin',
    defaults={'email': 'admin@example.com', 'first_name': 'Administrador', 'last_name': 'Principal', 'is_staff': True, 'is_superuser': True}
)
if created:
    admin_user.set_password('AdminPass123!')
    admin_user.save()
    print("Usuario admin creado (contraseña: AdminPass123!)")

# 2. Crear Usuario regular para pruebas
test_user, created_test = User.objects.get_or_create(
    username='developer',
    defaults={'email': 'dev@example.com', 'first_name': 'Carlos', 'last_name': 'Bocangel'}
)
if created_test:
    test_user.set_password('DevPass123!')
    test_user.save()
    profile, _ = Profile.objects.get_or_create(user=test_user)
    profile.bio = "Desarrollador de software y entusiasta del ecosistema Python / Django."
    profile.website = "https://github.com"
    profile.save()
    print("Usuario developer creado (contraseña: DevPass123!)")

# 3. Crear Artículos de Prueba
posts_data = [
    {
        'title': 'Bienvenido a DevBlog: Arquitectura y Buenas Prácticas con Django',
        'subtitle': 'Una guía completa sobre cómo estructurar proyectos web robustos y modulares',
        'content': '''Django es un framework de alto nivel para el desarrollo rápido y con un diseño limpio y pragmático.
Construido por programadores experimentados, se encarga de gran parte de la molestia del desarrollo web, para que puedas concentrarte en escribir tu aplicación sin necesidad de reinventar la rueda.

En este blog consolidado abordamos conceptos fundamentales:
1. Arquitectura MVT (Modelo - Vista - Template).
2. Seguridad de rutas mediante LoginRequiredMixin.
3. Separación de lógica con decouple y variables de entorno (.env).
4. Persistencia relacional con SQLite y manejo multimedia con Pillow.

¡Explora las publicaciones, comenta ideas y crea tus propios artículos desde el botón superior!''',
        'author': test_user,
    },
    {
        'title': 'El Camino del Desarrollador: De Python Básico a Aplicaciones Web Reales',
        'subtitle': 'Reflexiones sobre el proceso formativo desde los scripts de consola hasta el despliegue',
        'content': '''El recorrido de programación comienza con variables, estructuras de control de flujo y colecciones en memoria.
Luego, pasamos a la Programación Orientada a Objetos (POO), donde el código adquiere modularidad, encapsulación y escalabilidad.

El salto a Django representa el punto donde todas esas piezas convergen: los modelos encapsulan las tablas de la base de datos, las vistas procesan la lógica del negocio mediante funciones o clases genéricas (Class-Based Views), y los templates renderizan interfaces interactivas para el usuario final.''',
        'author': test_user,
    },
    {
        'title': 'Gestión Profesional de Repositorios en GitHub',
        'subtitle': 'Claves para entregar código limpio, reproducible y fácil de evaluar',
        'content': '''Un buen repositorio de GitHub debe ser autosuficiente:
- Un .gitignore que evite subir basura como venv/, __pycache__/ o archivos de bases de datos locales no deseadas.
- Un requirements.txt con las versiones exactas para poder replicar el entorno con un solo comando.
- Un README.md detallado con el paso a paso de instalación, configuración e inicio del servidor.
- Un historial de commits semántico que demuestre la evolución del proyecto paso a paso.''',
        'author': admin_user,
    }
]

for p in posts_data:
    post_obj, created_p = Post.objects.get_or_create(
        title=p['title'],
        defaults={
            'subtitle': p['subtitle'],
            'content': p['content'],
            'author': p['author']
        }
    )
    if created_p:
        print(f"Post creado: '{post_obj.title}'")

print("Seeding de datos completado.")
