
from django.urls import path, include

from dataentry.views import importData

urlpatterns = [
    path('import-data', importData, name='import_data'),
]