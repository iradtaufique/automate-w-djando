from django.core.management.base import BaseCommand

from dataentry.models import Students


class Command(BaseCommand):
    help = "Inserting Data to our database"

    def handle(self, *args, **kwargs):
        """logic goes here"""

        #Todo: insert a list of user from dataset
        dataset = [
            {'roll_no': 1001, 'name': 'John', 'age': 10},
            {'roll_no': 1002, 'name': 'Doe', 'age': 11},
            {'roll_no': 1003, 'name': 'Peter', 'age': 12},
            {'roll_no': 1004, 'name': 'Cyusa', 'age': 13},
        ]

        for data in dataset:
            #todo: insert this data in student table
            Students.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])

        self.stdout.write(self.style.SUCCESS('Data Entered Successfully'))