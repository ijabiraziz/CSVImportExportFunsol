
from django.urls import path
from .views import export_csv, import_csv

urlpatterns = [
    path('export/', export_csv, name='export_csv'),
    path('import/', import_csv, name='import_csv'),
]

