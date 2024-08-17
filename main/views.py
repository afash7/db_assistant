from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ExcelFile
import pandas as pd

def index(request):
    return render(request, 'index.html')

def upload_excel(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            df = pd.read_excel(file)
            html = df.to_html()
            return render(request, 'excel.html', {'html': html})
        else:
            return HttpResponse('فایلی ارسال نشده است')
    return render(request, 'upload.html')


def edit_excel(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            df = pd.read_html(content)[0]
            df.to_excel('output.xlsx', index=False)
            return HttpResponse('فایل اکسل ویرایش شده با موفقیت ذخیره شد.')
        else:
            return HttpResponse('محتوای فایل اکسل خالی است.')
    return render(request, 'edit_excel.html')