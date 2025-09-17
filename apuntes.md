# Capítulo 9

## 1. Activación del Entorno Virtual

Para trabajar en el proyecto, primero necesitas activar el entorno virtual de Python.

### Permisos de ejecución en Windows (PowerShell)
Si es la primera vez que abres la terminal, es posible que necesites ejecutar este comando para permitir la ejecución de scripts locales.

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

### Script de activación
Una vez configurados los permisos, utiliza este comando para activar el entorno. Tu prompt de la terminal cambiará para mostrar `(venv)`.

```powershell
.\venv\Scripts\activate.ps1
```

### Link de localhost
`/docs` permite acceder al `swagger` integrado de FastAPI
```link
localhost:5000/docs
```

---

## 2. Comandos Útiles

`uvicorn` es el servidor que usaremos para ejecutar nuestra aplicación FastAPI.

### Arrancar el servidor local
Este es el comando principal para poner en marcha tu aplicación. Debes ejecutarlo desde la carpeta raíz de tu proyecto.

```bash
uvicorn main:app --port 5000 --reload
```

#### Desglose de los parámetros más comunes:

* **`main:app`**:
    * `main`: Es el nombre del fichero Python (`main.py`) que contiene tu aplicación.
    * `app`: Es la variable dentro de `main.py` que crea la instancia de FastAPI (ej: `app = FastAPI()`).
* **`--reload`**: ¡Tu mejor amigo durante el desarrollo! Reinicia el servidor automáticamente cada vez que guardas un cambio en el código.
* **`--port 5000`**: Modifica el puerto de escucha. Por defecto, `uvicorn` usa el puerto `8000`.
* **`--host 0.0.0.0`**: (Opcional) Permite que otros dispositivos en tu misma red accedan a tu servidor. Por defecto es `127.0.0.1` (solo accesible desde tu propio PC).