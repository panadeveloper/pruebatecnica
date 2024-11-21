from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DatabaseConfig
from django.db import connections, transaction

class DataExtractionView(APIView):
    def post(self, request):
        config_id = request.data.get("config_id")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        
        if not all([config_id, start_date, end_date]):
            return Response({"error": "Faltan parámetros obligatorios (config_id, start_date, end_date)"}, status=400)

        try:
            config = DatabaseConfig.objects.get(id=config_id)
            query = config.query + f" WHERE fecha >= '{start_date}' AND fecha <= '{end_date}'"

            with connections['secondary'].cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()

            with connections['secondary'].cursor() as cursor:
                for row in data:
                    cursor.execute(
                        """
                        INSERT INTO api_factura(id, fecha, total, cliente_id, descripcion)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (id) DO UPDATE SET
                            fecha = EXCLUDED.fecha,
                            total = EXCLUDED.total,
                            cliente_id = EXCLUDED.cliente_id,
                            descripcion = EXCLUDED.descripcion
                        """,
                        row
                    )

            return Response({"message": "Los datos se han extraído y guardado satisfactoriamente en la base de datos secundaria.", "data": data}, status=200)

        except DatabaseConfig.DoesNotExist:
            return Response({"error": "Configuración de base de datos no encontrada"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
    def get(self, request):
        
        try:
            
            config_id = request.query_params.get("config_id", 1)
            config = DatabaseConfig.objects.get(id=config_id)
            
            data = {
                "host": config.host,
                "port": config.port,
                "namedb": config.namedb,
                "user": config.user,
                "password": config.password,
                "query": config.query    
            }
            
            with connections['secondary'].cursor() as cursor:
                cursor.execute("SELECT 1")
                
            return Response({"message": "CONEXIÓN EXITOSA CON LA BASE DE DATOS SECUNDARIA", "config":data}, status=200)
        
        except DatabaseConfig.DoesNotExist:
            return Response({"ERROR": "DatabaseConfig CON EL ID ESPECIFICADO NO EXISTE"}, status=404)
        
        except Exception as e:
            return Response({"ERROR": str(e)}, status=500)

                
