from django.core.management.base import BaseCommand

from dataentry.models import Students


"""
 ------ HOW TO RUN THIS COMMAND ---------
    ./MANAGE.PY FILENAME(inserData)
    EXAMPLE: ./MANAGE.PY INSERTDATA 
"""


class Command(BaseCommand):
    help = "Inserting Data to our database"

    def handle(self, *args, **kwargs):
        """logic goes here"""

        #Todo: insert a list of user from dataset
        dataset = [
            {'roll_no': 1001, 'name': 'John', 'age': 10},
            {'roll_no': 1002, 'name': 'Doe', 'age': 11},
            {'roll_no': 1005, 'name': 'Hope', 'age': 15},
            {'roll_no': 1004, 'name': 'Cyusa', 'age': 13},
            {'roll_no': 1006, 'name': 'Kate', 'age': 16},
        ]

        #todo: creating a variables that will count records are existed and new records
        new_rec_num =0
        exst_rec_num =0
        for data in dataset:
            #todo: adding validation check
            reg_no = data['roll_no']
            existing_record = Students.objects.filter(roll_no=reg_no).exists()

            if not existing_record:
                #todo: insert this data in student table
                new_rec_num += 1
                Students.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])

            else:
                exst_rec_num += 1
                self.stdout.write(self.style.WARNING(f"User with this ID {data['roll_no']} already exists!"))

        self.stdout.write(self.style.SUCCESS(f"Process Ended Successfully {new_rec_num} Entered in database and {exst_rec_num} Already Existed!"))