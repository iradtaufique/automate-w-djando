from django.core.management.base import BaseCommand


"""
 ------ HOW TO RUN THIS COMMAND ---------
    ./MANAGE.PY FILENAME(GREETING) NAMETOGREAT
    EXAMPLE: ./MANAGE.PY GREETING PETER
"""
class Command(BaseCommand):
    help = "This greeting Command Will Great User"

    """adding a method that will be parsed in kwarg parameter of handler method"""
    def add_arguments(self, parser):
        """parser will allow to run command with
        extra argument on the command"""
        parser.add_argument('name', type=str, help='Specify the User Name')

    """Program Logic Entry"""
    def handle(self, *args, **kwargs):
        usrName = kwargs['name']
        greeting = f'Hi {usrName}, Good Morning Welcome!'
        self.stdout.write(greeting)

        """show greeting as an Error"""
        #self.stderr.write(greeting)
        """show greeting as a success Message"""
        #self.stdout.write(self.style.SUCCESS(greeting))