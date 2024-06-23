import csv
from django.core.management.base import BaseCommand
from foodtruck.models import Foodtruck

class Command(BaseCommand):
    help="load food truck data from CSV file"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file path')


    def handle(self, *args, **kwargs):
        file_path=kwargs['csv_file']
        with open(file_path,'r',encoding="UTF-8") as file:
            reader=csv.DictReader(file)
            for row in reader:
                Foodtruck.objects.create(
                    name=row['Applicant'],
                    latitude=float(row['Latitude']),
                    longitude=float(row['Longitude']),
                    address=row['Location']
                )

                self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
