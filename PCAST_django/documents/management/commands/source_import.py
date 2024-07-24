import csv
import re
from django.core.management.base import BaseCommand, CommandError
from documents.models import Document, LegacySubjects
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PCAST_django.settings')
django.setup()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PCAST_django.settings')
django.setup()

class Command(BaseCommand):
    help = 'imports legacy csv from jordan -- purpose-built'

    def handle(self, *args, **options):
        basepath = "documents/management/commands/"

        headers = [
            'Asset ID', 'Quartex UniqueIdentifier', 'Quartex Name', 'Collection(s)', 'Published URL', 'Title',
            'People and Organizations', 'Location', 'Approximate Date', 'Abstract', 'Description', 'Identifier',
            'Language', 'Publisher', 'Date', 'Rights', 'Source', 'Subject', 'Format Genre', 'Format', 'Repository',
            'Special Collections', 'University Archives', 'Time Span', 'Date Digital', 'Digitization Specifications',
            'Original Handle', 'Rights Summary', 'Accessibility Feature', 'Accessibility Summary', 'Legacy Subjects'
        ]

        print("Files in basepath:", os.listdir(basepath))

        csvs = [i for i in os.listdir(basepath) if i == 'pcast-etc-metadata-report.csv']
        print("csvs to read in", csvs)

        for this_csv in csvs:
            fpath = os.path.join(basepath, this_csv)
            print("full path to this csv", fpath)
            with open(fpath, 'r', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                headers = reader.fieldnames
                print("CSV Headers:", headers)
                for row in reader:
                    asset_id = row['Asset ID']
                    source = row['Source']

                    try:
                        document = Document.objects.get(asset_id=asset_id)
                        document.source = source
                        document.save()
                        print(f"Updated source for document with Asset ID {asset_id}")
                    except Document.DoesNotExist:
                        print(f"Document with Asset ID {asset_id} does not exist, skipping.")
pass