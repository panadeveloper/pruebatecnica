from .models import DatabaseConfig
from .views import DatabaseConfigViewSet


def daily_extraction():
    configs = DatabaseConfig.objects.all()
    for config in configs:
        DatabaseConfigViewSet.extract_data(None, config.id)