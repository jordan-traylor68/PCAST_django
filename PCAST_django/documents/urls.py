from django.urls import path,include
from .views import help_page
from . import views
from . import doc_api

urlpatterns = [
	path('',views.Gallery),
	path('<int:pagenumber>',views.Gallery,name='gallery'),
	path('single/<int:doc_id>',views.SingleDoc,name="doc_page"),
    path('admin/help/', help_page, name='admin_help'),
    path('api/doc/<int:pk>/', doc_api.DocDetailAPIView.as_view(), name='api-doc-detail'),
]
