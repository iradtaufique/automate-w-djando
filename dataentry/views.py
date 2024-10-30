from django.shortcuts import render

from dataentry.utils import get_all_custom_models


# Create your views here.

def importData(request):
    if request.method == 'POST':
        return
    else:
        all_models = get_all_custom_models()
        context = {
            'all_models': all_models
        }
    return render(request, 'data-entry/import_data.html', context)
