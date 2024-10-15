from os import write

from django.core.management import BaseCommand
from dataentry.models import Students
import datetime
import csv

class Command(BaseCommand):
    help = 'Export data from student model'

    def handle(self, *args, **kwargs):
        """fetch data from database"""
        student_data = Students.objects.all()

        #Generate timestamp y-m-d-h-m-s
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        """define the csv file name path"""
        file_path = f"exported_student_data_{timestamp}.csv"

        """Open the csv file and write data into csv file"""
        #todo: the newline will add new line after evey row
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)

            """write the CSV Header"""
            writer.writerow(['Roll No', 'Name', 'Age'])

            """write Data rows"""
            for student in student_data:
                writer.writerow([student.roll_no, student.name, student.age])

        self.stdout.write(self.style.SUCCESS("Data Exported Successfully"))
