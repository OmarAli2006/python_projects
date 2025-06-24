# Entorno Virtual de Python para Manim

## Activación del Entorno Virtual

### En Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

Si tienes problemas con la ejecución de scripts en PowerShell, puede que necesites cambiar la política de ejecución:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### En Windows (Command Prompt)

```cmd
venv\Scripts\activate.bat
```

## Instalación de Paquetes

Una vez activado el entorno virtual, puedes instalar paquetes usando pip:

```
pip install manim
```

## Desactivación del Entorno Virtual

Para desactivar el entorno virtual, simplemente ejecuta:

```
deactivate
```

## Nota

Recuerda que debes activar el entorno virtual cada vez que abras una nueva terminal para trabajar en este proyecto.