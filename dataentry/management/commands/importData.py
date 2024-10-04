import csv
from dataentry.models import Students
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Commands to import CSV file"
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="File Path")

    def handle(self, *args, **kwargs):
        #todo: this is variable that will store the path of the file
        myfile = kwargs['file_path']

        """variable used To count records"""
        new_rec_num = 0
        exst_rec_num = 0

        #todo: opening the csv file
        with open(myfile, 'r') as file:
            #todo: read the file as a dictionary
            reader = csv.DictReader(file)
            for data in reader:
                #todo: make some custom validation to check if data exists
                data_exist = Students.objects.filter(roll_no=data['roll_no']).exists()
                if not data_exist:
                    """the **data will insert data at the same time instead of writing one at time"""
                    Students.objects.create(**data)
                    new_rec_num += 1
                else:
                    exst_rec_num += 1
                    self.stdout.write(f"Record with ROll Number {data['roll_no']} already Exist in Table")

        self.stdout.write(self.style.SUCCESS(
            f"{new_rec_num} Record imported Successfully in database and {exst_rec_num} record already Existed!"))

