from django.urls import path,include
from .views import help_page
from . import views
from . import doc_api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'doc', doc_api.DocViewSet)

urlpatterns = [
	path('',views.Gallery),
	path('<int:pagenumber>',views.Gallery,name='gallery'),
	path('single/<int:doc_id>',views.SingleDoc,name="doc_page"),
    path('admin/help/', help_page, name='admin_help'),
    path('api/', include(router.urls)),
]
