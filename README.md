# API Compañía

Pequeña API con FastAPI y SQLAlchemy para manejar información de compañías.
Por: Santiago Garzón Chica

## Modelo

```json
{
  "name": "Google",
  "web": "www.google.com",
  "year": 2006,
  "id": 1
}
```

## Endpoints

| Método | Ruta | Descripción |
|--------|------|--------------|
| GET | `/companies/` | Lista todas las compañías |
| GET | `/companies/{id}` | Obtiene una compañía por su ID |
| POST | `/companies/` | Crea una nueva compañía |
| PUT | `/companies/{id}` | Actualiza una compañía existente |
| DELETE | `/companies/{id}` | Elimina una compañía |

## Ejecución

1. Instalar dependencias:
   ```bash
   pip install fastapi[all] sqlalchemy
   ```

2. Ejecutar el servidor:
   ```bash
   python main.py
   ```

3. Abrir la documentación interactiva:
   - Swagge: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)
