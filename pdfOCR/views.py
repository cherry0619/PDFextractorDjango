from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import os

from .utils.pdfExtractor import FicoScore,bereauExtract

file_name =""


def extractor(request):
    if request.method == 'POST' and request.FILES['myfile']:
        pdf_file = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(pdf_file.name, pdf_file)
        uploaded_file_url = fs.url(filename)
        global file_name
        file_name = pdf_file.name
        return render(request, 'pdfOCR/extractor.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'pdfOCR/extractor.html')


def pdfOCR(request):
    # read file from media and extract information
    pdf_path =os.path.join(settings.MEDIA_ROOT,file_name)
    print('pdf path is ',pdf_path)
    Fico_score = FicoScore(pdfPath=pdf_path, pageNum=0)
    bereau_summary = bereauExtract(pdfPath=pdf_path,pageNum=1)

    response_data = {'scoreSummary': Fico_score,"bereauSummary":bereau_summary}
    return JsonResponse(response_data)

def merger(request):
    my_context = {}
    return render(request,"pdfOCR/merger.html",context=my_context)


def pdf2word(request):
    my_context = {}
    return render(request,"pdfOCR/word.html",context=my_context)


def about(request):
    print("this is the about view")
    my_context = {}
    return render(request,"pdfOCR/word.html",context=my_context)



def simple_upload(request):
    print("this is the file uplaod view~~")
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'pdfOCR/extractor.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'pdfOCR/extractor.html')





# Create your views here.
# def extractor(request):
#     my_context = {'my_var': 'Hello, world!'}
#     return render(request,"pdfOCR/index.html",my_context)
#
# def upload_file(request):
#     file_url =''
#     if request.method == 'POST' and request.FILES['file']:
#         uploaded_file = request.FILES['file']
#         fs = FileSystemStorage()
#         filename = fs.save(uploaded_file.name, uploaded_file)
#         file_url = fs.url(filename)
#     html_content = render(request, 'pdfOCR/index.html',  {'file_url': file_url}).content
#     return JsonResponse({'html_content': html_content})