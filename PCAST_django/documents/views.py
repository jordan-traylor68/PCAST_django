from django.http import Http404, HttpResponse, HttpResponseForbidden, JsonResponse
from django.template import loader
from django.shortcuts import redirect,render
from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from documents.models import *

# Create your views here.


def Gallery(request,pagenumber=1):
	

	docs=Document.objects.all()
	docs=docs.order_by('id')
	docs_paginator=Paginator(docs, 12)
	this_page=docs_paginator.get_page(pagenumber)
	
# 		print(other_collections)
	
	return render(
		request,
		"gallery.html",
		{
			"page_obj": this_page
		}
	)
		
#######################
# then the individual page view
def SingleDoc(request,doc_id=1):

# 		print(zotero_source_id)
	doc=Document.objects.get(id=doc_id)
	
# 		print(doc)
	return render(request, "single_doc.html", {'doc':doc})