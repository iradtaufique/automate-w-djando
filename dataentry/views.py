from django.shortcuts import render, redirect

from dataentry.utils import get_all_custom_models
from uploads.models import Uploads
from django.conf import settings
from django.core.management import call_command


# Create your views here.

def importData(request):
    if request.method == 'POST':
        """getting the file name and model name from the user form"""
        file_name = request.FILES.get('file_name')
        model_name = request.POST.get('model_name')

        print(file_name)
        print(model_name)

        """store this info in upload model"""
        upload = Uploads.objects.create(file=file_name, model_name=model_name)

        """Construct the full path of file"""
        relative_path = str(upload.file.url)
        base_url = str(settings.BASE_DIR)

        file_path = base_url + relative_path
        """trigger the import command which will help to run the import command from
        management/commands folder"""
        try:
            call_command('importData1', file_path, model_name)
        except Exception as e:
            raise e


        return redirect('import_data')
    else:
        all_models = get_all_custom_models()
        context = {
            'all_models': all_models
        }
    return render(request, 'data-entry/import_data.html', context)
