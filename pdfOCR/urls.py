from django.urls import path
from . import views

urlpatterns = [
    path('extractor', views.extractor,name="extractor"),
    path('merger',views.merger,name='merger'),
    path('word', views.pdf2word, name='word'),
    path('about', views.about, name='about'),
    path('pdfOCR', views.pdfOCR, name='pdfOCR'),

]