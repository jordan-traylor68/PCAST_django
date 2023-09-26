from django.urls import path,include
from . import views

urlpatterns = [
	path('',views.Gallery),
	path('<int:pagenumber>',views.Gallery,name='gallery'),
	path('single/<int:doc_id>',views.SingleDoc,name="doc_page")
]
