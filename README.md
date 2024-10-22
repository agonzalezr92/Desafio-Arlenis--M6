# Proyecto Django: Lista de Empleados

Este es un proyecto simple en Django que muestra una lista de nombres de empleados en una página web.

## Requisitos

- Python 
- Django

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/nombre-del-repo.git

2. **Crea y activa un entorno virtual:**

cd nombre-del-repo
python -m venv myenv

# Activar el entorno virtual
# En Windows:
myenv\Scripts\activate
# En macOS/Linux:
source myenv/bin/activate

3. **Instala Django:**

   pip install django

4. **Ejecuta las migraciones:**
   python manage.py migrate
  
5. **Ejecuta el servidor de desarrollo:**
python manage.py runserver

6. **Accede a la aplicación:**
   Abre tu navegador y visita http://127.0.0.1:8000/empleados/ para ver la lista de empleados.

  **Estructura del Proyecto**

    myproject/: Carpeta del proyecto principal.
        empleados/: Carpeta de la aplicación que contiene la lógica para mostrar la lista de empleados.
            templates/: Carpeta que contiene los templates HTML.
                empleados/: Carpeta que contiene los templates específicos de la aplicación empleados.
                    lista.html: Template que muestra la lista de empleados.
