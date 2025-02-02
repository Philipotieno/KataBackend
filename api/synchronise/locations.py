import csv

from django.core import management
from django.utils.text import slugify

from locations.models import StudyArea

def synchronise_study_area(self, csv_file):
    """ Imports StudyArea objects from data/areas.csv """
    if hasattr(self, 'stdout'):
        self.stdout.write(self.style.MIGRATE_LABEL("StudyArea:"))

    with open(csv_file, 'rt') as areas_csv:
        areas_reader = csv.DictReader(areas_csv, delimiter=',', quotechar='"')

        created_count = 0
        checked_count = 0

        for row in areas_reader:
            name_slugified = slugify(row['Study area'])

            # Map fields
            area_map = {
                'name': row['Study area'],
                'slug': name_slugified,
            }

            # Save as StudyArea object
            try:
                area = StudyArea.objects.get(slug=name_slugified)
                for key, value in area_map.items():
                    setattr(area, key, value)
                area.full_clean()
                area.save()
                checked_count += 1
            except StudyArea.DoesNotExist:
                area = StudyArea(**area_map)
                area.full_clean()
                area.save()
                created_count += 1

    if hasattr(self, 'stdout'):
        self.stdout.write("\tChecked: %d" % checked_count)
        self.stdout.write("\tCreated: %d" % created_count)
