from django.shortcuts import render

def home(request):
    return render(request, 'reports/home.html')

def report_fault(request):
    return render(request, 'reports/report_fault.html')
