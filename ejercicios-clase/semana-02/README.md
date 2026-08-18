# Semana 02 - Configuracion del Entorno y Buenas Practicas

En esta sesion se configuro el entorno virtual del curso y se aplicaron convenciones de estilo PEP 8 y anotaciones de tipo (Type Hints).

## Configuracion y Activacion del Entorno

Desde la raiz del repositorio:

```powershell
# Crear el entorno virtual
python -m venv venv

# Activar en Windows PowerShell
.\venv\Scripts\Activate.ps1

# Activar en Linux/macOS
source venv/bin/activate

Para instalar las dependencias exactas del proyecto:

# powershell 
pip install -r requirements.txt

