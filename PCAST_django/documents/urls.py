from django.urls import path,include
from .views import help_page
from . import views

urlpatterns = [
	path('',views.Gallery),
	path('<int:pagenumber>',views.Gallery,name='gallery'),
	path('single/<int:doc_id>',views.SingleDoc,name="doc_page"),
    path('admin/help/', help_page, name='admin_help')
]
