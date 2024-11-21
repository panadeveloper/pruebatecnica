from .models import DatabaseConfig
from django.db import connections
from datetime import datetime

def extract_data_daily():
    try:
        config = DatabaseConfig.objects.get(id=1)
        query = config.query  

        with connections['secondary'].cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()

        print(f"Datos extraídos automáticamente: {data}")

    except DatabaseConfig.DoesNotExist:
        print("Error: Configuración de base de datos no encontrada.")
    except Exception as e:
        print(f"Error al extraer datos: {str(e)}")
