from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """this line help line will be displayed at the top
    of command when --help run on this custom command"""

    help = "Prints Hello World Text"

    """this method is used as an entry point for all
     commands we need to run"""

    def handle(self, *args, **options):
        """This is where we write our logic"""
        # print hello World
        self.stdout.write("Helle World")