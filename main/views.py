from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ExcelFile
import pandas as pd

def read_excel(request):
    if request.method == 'POST':
        file = request.FILES['file']
        excel_file = ExcelFile(file=file)
        excel_file.save()
        df = pd.read_excel(file)
        return render(request, 'excel.html', {'df': df})
    return render(request, 'upload.html')

def edit_excel(request):
    if request.method == 'POST':
        file_id = request.POST['file_id']
        excel_file = ExcelFile.objects.get(id=file_id)
        df = pd.read_excel(excel_file.file)
        # ویرایش فایل اکسل
        df['column_name'] = 'new_value'
        df.to_excel(excel_file.file, index=False)
        return redirect('read_excel')
    return render(request, 'edit.html')