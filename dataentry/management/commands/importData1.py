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

        print('this works1')
    def handle(self, *args, **kwargs):
        #todo: this is variable that will store the path of the file
        myfile = kwargs['file_path']
        mymodel_name = kwargs['model_name'] #variable that will store model name.

        """variable used To count records"""
        new_rec_num = 0
        exst_rec_num = 0

        """
        for loop to search the name of model specified within the whole project apps
        """
        print(mymodel_name.capitalize())
        model = None
        for app_config in apps.get_app_configs():
            """ using try to search model"""
            try:
                model = apps.get_model(app_config.label, mymodel_name)
                break # this will break/stop once the model is found
            except LookupError:
                continue # once the mode is not found in app go search in the next app

        if not model:
            raise CommandError(f'Model {mymodel_name} Not found in Project')

        print(model)

        #todo: opening the csv file
        with open(myfile, 'r') as file:
            #todo: read the file as a dictionary
            reader = csv.DictReader(file)
            for data in reader:
                model.objects.create(**data)
        self.stdout.write(self.style.SUCCESS(f"Record imported Successfully in Database!"))

