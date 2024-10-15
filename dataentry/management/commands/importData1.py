import csv
from dataentry.models import Students
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps


"""
Proposed Command: ./manage.py importData1 csv_file_path model_name
"""

class Command(BaseCommand):
    help = "Commands to import CSV file"
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="CSV File Path")
        parser.add_argument('model_name', type=str, help="Name of the Model we need to import")

    def handle(self, *args, **kwargs):
        #todo: this is variable that will store the path of the file
        myfile = kwargs['file_path']
        mymodel_name = kwargs['model_name'].capitalize() #variable that will store model name.

        model = None
        for app_config in apps.get_app_configs():
            """ using try to search model"""
            try:
                model = apps.get_model(app_config.label, mymodel_name)
                break # this will break/stop once the model is found
            except LookupError:
                continue # once the mode is not found in app go search in the next app

        if not model:
            raise CommandError(f'No Model Name {mymodel_name} found in our app')

        #todo: opening the csv file
        with open(myfile, 'r') as file:
            #todo: read the file as a dictionary
            reader = csv.DictReader(file)
            for data in reader:
                """
                i will need to add the validation which will not be the ID, 
                maybe something else because the model will not be the same
                always, to make it easier id will be ok but don't know if 
                the csv file will contain id fild
                """
                model.objects.create(**data)
        self.stdout.write(self.style.SUCCESS(f"Record imported Successfully in Database!"))

