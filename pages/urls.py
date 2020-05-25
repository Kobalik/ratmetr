from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('addmarks', views.addMarks, name='addmarks'),
    path('addsubjects', views.addsubjects, name='addsubjects'),
    path('printdoc', views.printdoc, name='printdoc'),
    path('printPDF', views.printPDF, name='printPDF'),
    path('search', views.search, name='search'),
    path('searchStudent', views.searchStudent, name='searchStudent'),
    path('dashboard', views.dashboard, name='dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)