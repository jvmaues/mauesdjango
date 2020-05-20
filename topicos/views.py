from django.shortcuts import render

def index(request):
    return render( request, 'index.html')

def topico(request):
    return render(request, 'receita.html')


# Create your views here.
