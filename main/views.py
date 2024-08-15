from django.shortcuts import render

def display_excel(request):
    file_path = './files/MARKETING_REPORT.xlsx'
    table_html = read_excel_to_html(file_path)
    return render(request, 'myapp/display_excel.html', {'table_html': table_html})
