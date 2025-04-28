# Actividad: Módulo 3 - Lección 2

Este repositorio contiene una implementación de autenticación y autorización de usuarios utilizando Flask, Flask-Login y Flask-Principal.

Se protegen rutas específicas basadas en los roles de los usuarios: admin, editor y usuario normal.

## 📁 Estructura del Proyecto

```
flask-auth-roles-leccion2/
├── app.py                    # Código principal del servidor Flask
├── requirements.txt          # Dependencias necesarias
├── templates/
│   ├── login.html             # Página de inicio de sesión
│   ├── dashboard.html         # Panel principal después de login
│   ├── admin.html             # Sección restringida para admins
│   ├── editor.html            # Sección para admins y editores
│   └── denegado.html          # Página de acceso denegado (403)
└── README.md                  # Información del proyecto
```

## 🚀 Cómo ejecutar

1. Clonar este repositorio:

```bash
git clone https://github.com/Zeurodite/flask-auth-roles-leccion2.git
cd flask-auth-roles-leccion2
```

2. Crear y activar un entorno virtual:

```bash
python -m venv .venv
.\.venv\Scriptsctivate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutar la aplicación:

```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000/`

## 🔐 Roles y Rutas Protegidas

| Ruta        | Rol requerido  | Descripción                    |
|-------------|----------------|--------------------------------|
| `/dashboard`| Cualquier usuario autenticado | Acceso general |
| `/admin`    | Solo admin      | Acceso a funciones de administración |
| `/editor`   | Admin o Editor  | Acceso a funciones de edición |

## 🗂️ Funcionalidades

- Inicio de sesión
- Gestión de sesiones
- Control de acceso por roles
- Mensajes de error personalizados (403 Acceso Denegado)

## 📤 Entrega

Este proyecto forma parte de la entrega de la Lección 2 del Módulo 3.

Repositorio oficial:  
[https://github.com/Zeurodite/flask-auth-roles-leccion2](https://github.com/Zeurodite/flask-auth-roles-leccion2)

✍️ _Autor: Abdiel Rodríguez_  
📅 _Fecha: Abril 2025_
