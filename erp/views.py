from django.shortcuts import render

# Create your views here.
def main_view(request):
    if request.method == 'GET':
        return render(request, 'erp/main.html')