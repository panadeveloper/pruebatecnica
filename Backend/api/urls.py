from django.urls import path
from .views import DataExtractionView

urlpatterns = [
    path('extract-data/', DataExtractionView.as_view(), name='extract-data'),
]