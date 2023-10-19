import re
from django.core.management.base import BaseCommand, CommandError
from documents.models import *
import os
import requests
import json

class Command(BaseCommand):
    help = 'walks the iiif manifest link attached to each domucment and records the page images tha twe get from from it'
    def handle(self, *args, **options):
        #pull all our documents
        docs = Document.objects.all()
        #https://iiif.quartexcollections.com/rice/iiif/f451294b-e7b4-4338-9aca-873cf04b7d09/manifest
        for doc in docs:
            #print(doc.__dict__)
            quartex_uid=doc.quartex_uid
            #print(quartex_uid)
            manifest_url="https://iiif.quartexcollections.com/rice/iiif/%s/manifest" %quartex_uid
            print("MANIFEST -->", manifest_url)
            r = requests.get(manifest_url)
            if r.status_code!=200:
                print("uh-oh",r.status_code)
                exit()
            else:
                manifest_jason=r.text
                manifest_dict=json.loads(manifest_jason)
                #print(manifest_dict['metadata'],'\n-------')
                #we want 
                #"https://iiif.quartexcollections.com/rice/iiif/87d9d1a7-429c-4e54-a287-d3dffced4236/full/full/0/default.jpg"
                #they live in sequences/canvases/images
                sequences= manifest_dict['sequences']
                if len(sequences)>1:
                    print("WARNING! MULTIPLE SEQUENCES. ONLY DOING THE FIRST")
                sequence = sequences[0]
                canvases=sequence['canvases']
                pagenumber=1
                for canvas in canvases:
                    image=canvas['images']
                    if len(image)>1:
                        print("WARNING! MULTIPLE IMAGES ON THIS CANVAS. ONLY DOING THE FIRST")
                    image=image[0]
                    image_link=image['resource']['@id']
                    
                    print("IMAGE LINK-->",image_link)
					#https://iiif.quartexcollections.com/rice/iiif/3fe12e23-d2d5-476c-8341-6137b1edd0ac/full/full/0/default.jpg
                    iiif_hash=re.search('[a-z|0-9]+-[a-z|0-9]+-[a-z|0-9]+-[a-z|0-9]+-[a-z|0-9]+',image_link).group(0)
                    print(iiif_hash)

                    page,page_isnew=Pages.objects.get_or_create(
						quartex_image_iiif_hash=iiif_hash,
						order=pagenumber,
						document=doc
					)
                    pagenumber+=1