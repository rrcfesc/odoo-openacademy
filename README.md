# Construir un Módulo (Resumen)
## Estructura de un Módulo
1. Un módulo de Odoo es declarado por su manifiesto.
2. Un módulo es también un paquete de Python con un archivo __init__.py, que contiene instrucciones de importación de varios archivos de Python en dicho módulo.
3. Por ejemplo, si un módulo tiene un solo archivo mymodule.py, el archivo __init__.py podría contener:

```python
from . import mymodule
```

### Ayuda para crear un módulo
```bash
$ odoo-bin scaffold <module name> <where to put it>
```

## Mapeo Objeto-Relacional
Un componente clave de Odoo es el ORM. Esta capa evita escribir la mayoría del SQL
manualmente y proporciona extensibilidad y servicios de seguridad 2.

Los objetos de negocio se declaran como clases Python que extienden Model
 a cual los integra en el sistema automatizado de persistencia.

Módulos pueden ser configurados para establecer un número de atributos en su definición.
El atributo más importante es _name el cuál es requerido y define el nombre para el modelo en el sistema de Odoo. 
Aquí es mínimamente completada la definición de un modelo:

```python
from odoo import models
class MinimalModel(models.Model):
    _name = 'test.model'
```

### Campos en el Modelo 
Los campos se utilizan para definir lo que puede almacenar el modelo y dónde.
Los campos se definen como atributos en el modelo:
```python
from odoo import models, fields

class LessMinimalModel(models.Model):
    _name = 'test.model2'

    name = fields.Char()
```

