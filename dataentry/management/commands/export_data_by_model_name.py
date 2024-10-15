from dataclasses import field

from django.core.management import BaseCommand, CommandError
from dataentry.models import Students
import datetime
import csv
from django.apps import apps

class Command(BaseCommand):
    help = 'Export data from any model Name'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Specify Model Name')

    def handle(self, *args, **kwargs):
        """add model name argument"""
        myModelName = kwargs['model_name'].capitalize()

        """variable model that will act as any table"""
        model = None
        """loop in all apps of the project to find the model specifed"""
        for app_conf in apps.get_app_configs():
            try:
                model = apps.get_model(app_conf.label, myModelName)
                break # loop will break once model found
            except LookupError:
                pass

        if not model:
            raise CommandError(f'This Model name {myModelName} not found')
        """fetch data from database"""
        data = model.objects.all()

        #Generate timestamp y-m-d-h-m-s
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        """define the csv file name path"""
        file_path = f"exported_{myModelName}_data_{timestamp}.csv"

        """Open the csv file and write data into csv file"""
        #todo: the newline will add new line after evey row
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)

            """write the CSV Header"""
            #todo: _meta is the django api that will help to retrieve table fields
            writer.writerow([field.name for field in model._meta.fields])

            """write Data rows"""
            #todo: getattr method will help to get each individual column data in each row
            for dat in data:
                writer.writerow([getattr(dat, field.name) for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS("Data Exported Successfully"))
