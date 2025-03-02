from django.shortcuts import render
from django.db.models import Q
from multas.models import Multa

def home(request):
    query = request.GET.get('q', '')
    multas = []
    
    if query:
        multas = Multa.objects.filter(
            Q(codigo_infracao__icontains=query) |
            Q(infracao__icontains=query)
        )
    
    return render(request, 'home.html', {
        'multas': multas,
    }) 