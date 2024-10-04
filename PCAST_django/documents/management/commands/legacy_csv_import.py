import csv
import re
from django.core.management.base import BaseCommand, CommandError
# from documents import *
# from PCAST_django.documents.models import Document, LegacySubjects
from documents.models import Document, LegacySubjects
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PCAST_django.settings')
django.setup()

class Command(BaseCommand):
	help = 'imports legacy csv from jordan -- purpose-built'
	def handle(self, *args, **options):

		basepath="documents/management/commands/"

		headers=['Asset ID',
		'Quartex UniqueIdentifier',
		'Quartex Name',
		'Collection(s)',
		'Published URL',
		'Title',
		'People and Organizations',
		'Location',
		'Approximate Date',
		'Abstract',
		'Description',
		'Identifier',
		'Language',
		'Publisher',
		'Date',
		'Rights',
		'Source',
		'Subject',
		'Format Genre',
		'Format',
		'Repository',
		'Special Collections',
		'University Archives',
		'Time Span',
		'Date Digital',
		'Digitization Specifications',
		'Original Handle',
		'Rights Summary',
		'Accessibility Feature',
		'Accessibility Summary',
		'Legacy Subjects']
		print("Files in basepath:", os.listdir(basepath))


# if not csvs:
#     	print("No CSV files found.")
# else:
		csvs=[i for i in os.listdir(basepath) if i=='pcast-etc-metadata-report.csv']
		print("csvs to read in",csvs)
		for this_csv in csvs:
			fpath=os.path.join(basepath,this_csv)
			print("full path to this csv",fpath)
			with open(fpath,'r',encoding='utf-8-sig') as csvfile:
				reader=csv.DictReader(csvfile,delimiter='\t')
				headers=reader.fieldnames
				print("CSV Headers:", headers)
				for row in reader:
					title=row['Title']
					asset_id=row['Asset ID']
					quartex_uid=row['Quartex UniqueIdentifier']
					quartex_name=row['Quartex Name']
					lang=row['Language']
					
					row_doc,row_doc_isnew=Document.objects.get_or_create(
						quartex_uid=row['Quartex UniqueIdentifier'],
						defaults={
						'title': row['Title'],
						'asset_id': row['Asset ID'],
						'lang': row['Language'],
						'quartex_name':row['Quartex Name']
						}
					)
					
					legacy_subjects=row['Legacy Subjects'].split(',')
					
					for legacy_subject in legacy_subjects:
						#get or create returns a tuple
						##1. the object
						##2. a boolean: is it new?
						ls_obj,ls_obj_isnew=LegacySubjects.objects.get_or_create(
							name=legacy_subject
						)
						row_doc.subjects.add(ls_obj)
					row_doc.save()
pass
						
						
					
					
					
					
