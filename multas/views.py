from django.shortcuts import render
from .models import Multa
from django.db.models import Q

def buscar_multas(request):
    # Inicializa a query vazia
    query = request.GET.get('q', '')
    multas = []
    
    # Realiza a busca apenas se houver um termo de pesquisa
    if query:
        # Busca por código de infração ou descrição da infração
        multas = Multa.objects.filter(
            Q(codigo_infracao__icontains=query) |
            Q(infracao__icontains=query)
        )[:50]  # Limita a 50 resultados para melhor performance
    
    return render(request, 'multas/buscar.html', {
        'query': query,
        'multas': multas
    }) 