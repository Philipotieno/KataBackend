from django.core import management

from synchronise.locations import synchronise_study_area
from synchronise.birds import synchronise_Bird
from locations.models import StudyArea
from birds.models import Bird

class Command(management.BaseCommand):
    help = "Allows the import of tables exported from the Access database."

    def check_current_status(self):
        """ Outputs information about objects currently in database """
        self.stdout.write(self.style.MIGRATE_HEADING("Current status:"))
        self.stdout.write("StudyArea: %d" % StudyArea.objects.count())
        self.stdout.write("Bird: %d" % Bird.objects.count())

    def do_import(self):
        """ Imports objects into database """
        self.stdout.write(self.style.MIGRATE_HEADING("\nBeginning import:"))

        synchronise_study_area(self, "../test_data/tStudyAreas.csv")
        synchronise_Bird(self, "../test_data/Kea.csv")

        self.stdout.write(self.style.SUCCESS("\nImport complete"))

    def handle(self, *args, **options):
        self.check_current_status()

        #confirm = input("\nReady to import? Type 'yes' to continue: ")
        confirm = 'yes' # for debugging

        if confirm == 'yes':
            self.do_import()
        else:
            self.stdout.write("\nImport cancelled!")